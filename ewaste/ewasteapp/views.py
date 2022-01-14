from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.views.generic.edit import CreateView
from ewasteapp.forms import  objectTypeForm
from .models import Item

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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

def user_login(request):
    if request.method == "POST":
       username = request.POST["username"] 
       pass1 = request.POST['pass1']

       user = authenticate(username = username, password = pass1)
       if user is not None:
           login(request, user)
           fname = user.first_name
           return render(request, "index.html", {"fname":fname})
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
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = True
        myuser.save()
        
        messages.success(request, "Your account has been sucessfully created.")
        return redirect('login')
    return render(request, 'signup.html',)
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('login')
def driverlogin(request):
    return render(request, 'driverlogin.html')