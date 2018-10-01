from django.db import models


class kasutajad(models.Model):
    kasutajanimi = models.CharField(max_length=50, unique=True)
    parool = models.CharField(max_length=100)
