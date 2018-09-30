from django.db import models


class SignupModel(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
