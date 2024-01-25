from django.db import models

# Create your models here.

class Caffeine(models.Model):
    mg = models.IntegerField(default=0)
    time = models.TimeField(auto_now_add=True)

class Water(models.Model):
    oz = models.IntegerField(default=0)
    time = models.TimeField(auto_now_add=True)

class Exercise(models.Model):
    time = models.IntegerField(default=0)
    intensity = models.IntegerField()
    time = models.TimeField(auto_now_add=True)

class Sleep(models.Model):
    hours = models.FloatField()
    quality = models.BooleanField()
    awake = models.TimeField()
    time = models.TimeField(auto_now_add=True)