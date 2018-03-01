from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Profile, Recommendation

class IndexView(generic.ListView):
    template_name = 'viewlist/index.html'

    def get_queryset(self):
        """Return the last ten published questions."""
        return Profile.objects.order_by('-publish_date')

class ProfileDetail(generic.DetailView):
    model = Profile

class ProfileUpdate(generic.UpdateView):
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

class ProfileCreate(generic.CreateView):
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
  
def recommend(request, profile_id):
    return HttpResponse("You are writing a recommendation for profile %s." % profile_id)
