from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Profile, Recommandation

class IndexView(generic.ListView):
    template_name = 'viewlist/index.html'

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
        return reverse('viewlist:detail', args=(self.object.id,))

class CreateProfile(generic.CreateView):
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
            return reverse('viewlist:index')

class CreateRecommandation(generic.UpdateView):
    model = Recommandation
    fields = [
        'reviewer_name',
        'reviewer_email',
        'reviewer_position',
        'seen_at_conf',
        'comment',
    ]

    def get_success_url(self):
        return reverse('viewlist:detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return super(CreateRecommandation, self).form_valid(form)

class CreateRecommandation(generic.CreateView):
    model = Recommandation
    fields = [
        'reviewer_name',
        'reviewer_email',
        'reviewer_position',
        'seen_at_conf',
        'comment',
    ]

    def get_success_url(self):
        return reverse('viewlist:detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return super(CreateRecommandation, self).form_valid(form)