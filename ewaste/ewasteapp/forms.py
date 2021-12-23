from django.forms import ModelForm
from .models import Item
from django import forms
class objectTypeForm(ModelForm):
    class Meta:
        model = Item
        #fields = ['object_type']


