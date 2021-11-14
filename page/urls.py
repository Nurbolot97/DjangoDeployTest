from os import name
from django.urls import path
from . views import main, result


urlpatterns = [
    path('', main, name='main_page'),
    path('result/', result, name='result')
]







