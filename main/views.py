from django import views
from django.shortcuts import render, redirect
from django.views import View
from .models import *


class Index(View):
    def get(self, request):
        return render(request, 'index.html')

class About(View):
    def get(self, request):
        return render(request, 'about.html')