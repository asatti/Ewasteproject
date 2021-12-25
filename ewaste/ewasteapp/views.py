from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from ewasteapp.forms import  objectTypeForm, SignUpForm
from .models import Item
# Create your views here.
def home_page(request):
    return render(request, "index.html")
class ItemPickupView(CreateView):
    model = Item
    form_class = objectTypeForm
    template_name = 'pickup.html'
    success_url = 'pickup.html'
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = 'login.html'
    template_name = 'signup.html'
def pickup(request):
    return render(request, 'pickup.html',)

def postpickup(request):
    return render(request, 'postpickup.html',)

def login(request):
    return render(request, 'login.html',)

def signup(request):
    return render(request, 'signup.html',)

def driverlogin(request):
    return render(request, 'driverlogin.html')