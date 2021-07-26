from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views import generic

# Create your views here.
#def home_page(request):
    #return HttpResponse(index.html)
from django.views.generic.base import TemplateView


class HomeView(TemplateView):

    template_name = 'index.html'