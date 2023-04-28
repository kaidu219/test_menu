from .views import  MenuTestView, MenuView
from django.urls import path, include
from django.views.generic import View
from django.shortcuts import render, redirect

urlpatterns = [
    path('', MenuView.as_view(), name='home'),
    path('1', MenuTestView.as_view(), name='menu'),
]