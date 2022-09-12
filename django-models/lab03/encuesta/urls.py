from ast import pattern
from importlib.resources import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('',views.index,name='index')
]
