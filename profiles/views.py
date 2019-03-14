import re
from functools import reduce
from operator import and_, or_

from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q, Count
import pdb

from .models import Profile, Recommendation, Country
from .forms import CreateProfileModelForm, RecommendModelForm

class ListProfiles(ListView):
    template_name = 'profiles/list.html'
    context_object_name = 'profiles'
    model = Profile
    paginate_by = 20

    def get_queryset(self):
        searched_fields = ['name']
        s = self.request.GET.get('s')
        is_underrepresented = self.request.GET.get('ur') == 'on'
        is_senior = self.request.GET.get('senior') == 'on'

        q_st = ~Q(pk=None) # always true
        if s is not None:
            # split search terms and filter empty words (in case of successive spaces)
            search_terms = list(filter(None, s.split(' ')))

            for st in search_terms:
                st_regex = re.compile(f'.*{st}.*', re.IGNORECASE)

                # matching_positions = list(x[0] for x in Profile.get_position_choices() if st_regex.match(x[1]))
                matching_structures = list(Q(brain_structure__contains=x[0]) for x in Profile.get_structure_choices() if st_regex.match(x[1]))
                matching_modalities = list(Q(modalities__contains=x[0]) for x in Profile.get_modalities_choices() if st_regex.match(x[1]))
                matching_methods = list(Q(methods__contains=x[0]) for x in Profile.get_methods_choices() if st_regex.match(x[1]))
                matching_domains = list(Q(domains__contains=x[0]) for x in Profile.get_domains_choices() if st_regex.match(x[1]))

                st_conditions = [
                    Q(name__icontains=st),
                    Q(institution__icontains=st),
                    Q(position__icontains=st),
                    Q(brain_structure__icontains=st),
                    Q(country__name__icontains=st),
                    Q(keywords__icontains=st),
                 ] + matching_structures + matching_modalities + matching_methods + matching_domains

                q_st = and_(reduce(or_, st_conditions), q_st)

            

        if is_underrepresented:
            q_ur = Q(country__is_under_represented=True)
        else:
            q_ur = ~Q(pk=None) # always true

        if is_senior:
            senior_profiles_keywords = ('Senior', 'Lecturer', 'Professor', 'Director', 'Principal')
            # position must contain one of the words in the list (case insensitive)
            q_senior = reduce(or_, (Q(position__icontains=x) for x in senior_profiles_keywords))
        else:
            q_senior = ~Q(pk=None) # always true

        profiles_list = Profile.objects.filter(q_st, q_ur, q_senior).order_by('-publish_date')


        return profiles_list


class ProfileDetail(DetailView):
    model = Profile


class UpdateProfile(SuccessMessageMixin, UpdateView):
    model = Profile
    fields = [
        'name',
        'email',
        'webpage',
        'institution',
        'country',
        'position',
        'grad_month',
        'grad_year',
        'brain_structure',
        'modalities',
        'methods',
        'domains',
        'keywords',
    ]
    success_message = "The profile for %(name)s was updated successfully"

    def get_success_url(self):
        return reverse('profiles:detail', args=(self.object.id,))


class CreateProfile(SuccessMessageMixin, CreateView):
    template_name = 'profiles/profile_form.html'
    form_class = CreateProfileModelForm
    # success_url = reverse_lazy('profiles:index')
    success_message = "The profile for %(name)s was created successfully"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        form.save()
        return super().form_valid(form) 

    def get_success_url(self):
        return reverse('profiles:detail', kwargs={'pk': self.object.pk})

class CreateRecommendation(SuccessMessageMixin, FormView):
    template_name = 'profiles/recommendation_form.html'
    form_class = RecommendModelForm

    def get_success_url(self):
        return reverse('profiles:detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        form.save()
        return super(CreateRecommendation, self).form_valid(form)

def safe_div(x,y):
    if y == 0:
        return 0
    return x / y

def home(request):
    # Get stats on database for Home page:
    # Career stage
    senior_keywords = ('Senior', 'Lecturer', 'Professor', 'Director', 'Principal')
    nb_senior = Profile.objects.filter(reduce(or_, [Q(position__icontains=q) for q in senior_keywords])).count()
    nb_students = Profile.objects.filter(position__icontains='PhD student').count()
    nb_postdoc = Profile.objects.filter(position__icontains='Post-doc').count()
    nb_all = Profile.objects.count()
    # Number of entries per country
    country_stats = Profile.objects.all().values('country__name').annotate(total=Count('id'))

    context = {
        'nb_senior': nb_senior,
        'nb_all': nb_all,
        'nb_students' : nb_students,
        'nb_postdoc' : nb_postdoc,
        'nb_other' : nb_all - nb_senior - nb_students - nb_postdoc,
        'pct_students' : round(100*safe_div(nb_students, nb_all)),
        'pct_postdoc' : round(100*safe_div(nb_postdoc, nb_all)),
        'pct_senior' : round(100*safe_div(nb_senior, nb_all)),
        'pct_other' : round(100*safe_div((nb_all - nb_senior - nb_students - nb_postdoc), nb_all)),
        'country_stats': country_stats,
    }
    return render(request, 'profiles/home.html', context)
