from django.forms import ModelForm
from .models import Item
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class objectTypeForm(ModelForm):
    class Meta:
        model = Item
        fields = ['object_type']




