from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Profile, Recommendation

class IndexView(generic.ListView):
    template_name = 'viewlist/index.html'
    # context_object_name = 'latest_entries'

    def get_queryset(self):
        """Return the last ten published questions."""
        return Profile.objects.order_by('-publish_date')[:10]

class DetailView(generic.DetailView):
    model = Profile
    template_name = 'viewlist/detail.html'

class EditView(generic.DetailView):
    model = Profile
    template_name = 'viewlist/edit.html'
    
def add_profile_form(request):
    return render(request, 'viewlist/add.html')
    
def create_profile(request):
    profile = Profile()
    try:
        profile.name = request.POST['name']
        profile.email = request.POST['email']
        profile.webpage = request.POST['webpage']
        profile.institution = request.POST['institution']
        profile.country = request.POST['country']
        profile.position = request.POST['position']
        profile.grad_date = request.POST['grad_date']
        profile.brain_structure = request.POST['brain_structure']
        profile.modalities = request.POST['modalities']
        profile.methods = request.POST['methods']
        profile.domain = request.POST['domain']
        profile.keywords = request.POST['keywords']
        
    except (KeyError):
        # Redisplay the add form.
        return render(request, 'viewlist/add.html', {
            'error_message': "Error while submitting the data: %s" % str(KeyError)
        })
    else:
        profile.save();
        return HttpResponseRedirect(reverse('viewlist:index'))
    
def update_profile(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    try:
        profile.name = request.POST['name']
        profile.email = request.POST['email']
        profile.webpage = request.POST['webpage']
        profile.institution = request.POST['institution']
        profile.country = request.POST['country']
        profile.position = request.POST['position']
        # profile.grad_date = request.POST['grad_date']
        profile.brain_structure = request.POST['brain_structure']
        profile.modalities = request.POST['modalities']
        profile.methods = request.POST['methods']
        profile.domain = request.POST['domain']
        profile.keywords = request.POST['keywords']
    except (KeyError):
        # Redisplay the edit form.
        return render(request, 'viewlist/edit.html', {
            'profile': profile,
            'error_message': "Error while submitting the data: %s" % str(KeyError),
        })
    else:
        profile.save();
        return HttpResponseRedirect(reverse('viewlist:detail', args=(profile.id,)))
        
        
def recommend(request, profile_id):
    return HttpResponse("You are writing a recommendation for profile %s." % profile_id)