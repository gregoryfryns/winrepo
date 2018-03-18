from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.template import loader

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    # template = loader.get_template('about/index.html')
    return render(request, 'about/index.html')
