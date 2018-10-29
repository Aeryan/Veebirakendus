from django.db import models


class raamatud(models.Model):
    pealkiri = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    kirjastus = models.CharField(max_length=30)
    ilmumisaasta = models.IntegerField
    lehekülgi = models.IntegerField
    keel = models.CharField(max_length=10)


class wanted(models.Model):
    id = models.AutoField(primary_key=True)
    usr = models.IntegerField(default=0)
    book = models.ForeignKey(raamatud, to_field='id', on_delete=models.CASCADE, default=0)
    comment = models.CharField(max_length=300)


class owned(models.Model):
    id = models.AutoField(primary_key=True)
    usr = models.IntegerField(default=0)
    book = models.ForeignKey(raamatud, to_field='id', on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)


class tracking(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=30)
    brauser = models.CharField(max_length=30)
    os = models.CharField(max_length=30)
    time = models.DateTimeField()
