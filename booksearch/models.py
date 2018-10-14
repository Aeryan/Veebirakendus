from django.db import models


class raamatud(models.Model):
    pealkiri = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    kirjastus = models.CharField(max_length=30)
    ilmumisaasta = models.IntegerField
    lehekülgi = models.IntegerField
    keel = models.CharField(max_length=10)

