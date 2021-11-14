from django.forms import ModelForm
from .models import Data


class PageForm(ModelForm):
    class Meta:
        model = Data
        fields = ('name', 'surname', 'email', 'login', 'password')












