from django.db import models

class Salon(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    work_regime = models.CharField(max_length=100)

class Master(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    seniority = models.IntegerField()
    photo = models.ImageField()

class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    description = models.TextField()

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

