from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.views.generic.edit import CreateView
from ewasteapp.forms import  objectTypeForm
from .models import Item
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate
# Create your views here.
def home_page(request):
    return render(request, "index.html")
class ItemPickupView(CreateView):
    model = Item
    form_class = objectTypeForm
    template_name = 'pickup.html'
    success_url = 'pickup.html'

def pickup(request):
    return render(request, 'pickup.html',)

def postpickup(request):
    return render(request, 'postpickup.html',)

def login(request):
    if request.method == "POST":
       username = request.POST["username"] 
       pass1 = request.POST['pass1']

       user = authenticate(username = username, password = pass1)
       if user is not None:
           login(request,user)
           
           return render(request, "index.html")
       else:
            messages.error(request, "Bad Credentials")
            return redirect('login')
    return render(request, 'login.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        address = request.POST['address']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = CustomUser.objects.create_user(email, username, fname, lname, address, pass1)
        myuser.save()
        messages.success(request, "Your account has been sucessfully created.")
        return redirect('login')
    return render(request, 'signup.html',)

def driverlogin(request):
    return render(request, 'driverlogin.html')