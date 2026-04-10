from django import forms
from .models import Bb, IceCream


class BbForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = ['title', 'content', 'price', 'rubric']


class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['name', 'flavor', 'price', 'is_available']