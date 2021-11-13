from django import views
from django.shortcuts import render, redirect
from django.views import View
from .models import *


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class About(View):
    def get(self, request):
        return render(request, 'about.html', context={
            'spectrum': Spectrum.objects.all()
        })


class Masters(View):
    def get(self, request):

        context = {
            "masters": Master.objects.all(),
        }

        return render(request, 'masters.html', context)


class Vacancies(View):
    def get(self,request):
        context = {
            "vacancies": Vacancy.objects.all()
        }

        return render(request, 'vacancies.html', context)


class SalonPage(View):
    def get(self, request):
        return render(request, 'salon.html', context={
            'salons': Salon.objects.all()
        })


class Services(View):
    def get(self, request):
        return render(request, 'services.html', context={
            'services': Service.objects.all()
        })

class Sales(View):
    def get(self, request):
        return render(request, 'sales.html', context={
            'sales': Sale.objects.all()
        })