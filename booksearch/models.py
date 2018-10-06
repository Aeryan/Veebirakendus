from django.db import models


class kasutajad(models.Model):
    kasutajanimi = models.CharField(max_length=50, unique=True)
    parool = models.CharField(max_length=100)


class raamatud(models.Model):
    pealkiri = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    kirjastus = models.CharField(max_length=30)
    ilmumisaasta = models.IntegerField
    lehekülgi = models.IntegerField
    keel = models.CharField(10)

