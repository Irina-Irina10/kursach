from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('masters/', views.Masters.as_view(), name='masters'),
    path('vacancies/', views.Vacancies.as_view(), name='vacancies'),
    path('salon/', views.SalonPage.as_view(), name='salon'),
    path('services/', views.Services.as_view(), name="services"),
    path('sales/', views.Sales.as_view(), name="sales"),
]
