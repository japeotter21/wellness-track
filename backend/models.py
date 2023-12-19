from django.db import models

# Create your models here.

class Caffeine(models.Model):
    mg = models.IntegerField(default=0)
    time = models.TimeField()

class Exercise(models.Model):
    time = models.IntegerField(default=0)
    intensity = models.IntegerField()

class Sleep(models.Model):
    hours = models.FloatField()
    quality = models.BooleanField()