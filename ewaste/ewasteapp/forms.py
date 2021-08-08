from django.forms import ModelForm
from .models import Item
from django import forms
class MyModelForm(forms.Form):
    class Meta:
        model = Item
        fields = ('item')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].queryset = Item.objects.none()
