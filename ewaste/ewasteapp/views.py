from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
def home_page(request):
    return HttpResponse('polls/templates/index.html')
class HomeView(TemplateView):

    template_name = 'index.html'