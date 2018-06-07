from functools import reduce
from operator import and_, or_

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q, Count
import pdb;


from .models import Profile, Recommendation, Country
from .forms import CreateProfileModelForm

class ListProfiles(generic.ListView):
    template_name = 'profiles/list.html'

    def get_queryset(self):
        """Return the latest profiles first"""
        return Profile.objects.order_by('-publish_date')

class ProfileDetail(generic.DetailView):
    model = Profile


class UpdateProfile(SuccessMessageMixin, generic.UpdateView):
    model = Profile
    fields = [
        'name',
        'email',
        'webpage',
        'institution',
        'country',
        'position',
        'grad_date',
        'brain_structure',
        'modalities',
        'methods',
        'domains',
        'keywords',
    ]
    success_message = "The profile for %(name)s was updated successfully"

    def get_success_url(self):
        return reverse('profiles:detail', args=(self.object.id,))


class CreateProfile(SuccessMessageMixin, generic.FormView):
    template_name = 'profiles/profile_form.html'
    form_class = CreateProfileModelForm
    success_url = reverse_lazy('profiles:index')
    success_message = "The profile for %(name)s was created successfully"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        form.save()
        return super().form_valid(form)


# class UpdateRecommendation(generic.UpdateView):
#     model = Recommendation
#     fields = [
#         'reviewer_name',
#         'reviewer_email',
#         'reviewer_position',
#         'seen_at_conf',
#         'comment',
#     ]

#     def get_success_url(self):
#         return reverse('profiles:detail', kwargs={'pk': self.kwargs['pk']})


class CreateRecommendation(generic.CreateView):
    model = Recommendation
    fields = [
        'reviewer_name',
        'reviewer_email',
        'reviewer_position',
        'seen_at_conf',
        'comment',
    ]

    def get_success_url(self):
        return reverse('profiles:detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return super(CreateRecommendation, self).form_valid(form)

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
        'pct_students' : round(100*(nb_students/nb_all)),
        'pct_postdoc' : round(100*(nb_postdoc/nb_all)),
        'pct_senior' : round(100*(nb_senior/nb_all)),
        'pct_other' : round(100*((nb_all - nb_senior - nb_students - nb_postdoc)/nb_all)),
        'country_stats': country_stats,
    }
    return render(request, 'profiles/home.html', context)
