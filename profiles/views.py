from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Profile, Recommendation
from .forms import CreateProfileForm

class IndexView(generic.ListView):
    template_name = 'profiles/index.html'
    selected_tab = 'repository'

    def get_queryset(self):
        """Return the latest profiles first"""
        return Profile.objects.order_by('-publish_date')

class ProfileDetail(generic.DetailView):
    model = Profile

class UpdateProfile(generic.UpdateView):
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
        'domain',
        'keywords',
    ]

    def get_success_url(self):
        return reverse('profiles:detail', args=(self.object.id,))

class CreateProfile(generic.FormView):
    template_name = 'profiles/profile_form.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('profiles:index')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        form.save()
        return super().form_valid(form)

class UpdateRecommendation(generic.UpdateView):
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

    def form_valid(self, form):
        form.instance.profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return super(CreateRecommendation, self).form_valid(form)

def Home(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    # template = loader.get_template('about/index.html')
    return render(request, 'profiles/home.html')
