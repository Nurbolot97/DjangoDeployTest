from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.forms.models import model_to_dict
from .models import Data


class PageForm(ModelForm):
    class Meta:
        model = Data
        fields = ('name', 'surname', 'email', 'login')












