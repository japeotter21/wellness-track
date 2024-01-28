from django.db import models

# Create your models here.

class Caffeine(models.Model):
    mg = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

class Water(models.Model):
    oz = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

class Alcohol(models.Model):
    drinks = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

class Exercise(models.Model):
    time = models.IntegerField(default=0)
    intensity = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

class Sleep(models.Model):
    hours = models.FloatField()
    quality = models.IntegerField(default=1)
    awake = models.TextField(default="08:00")
    time = models.DateTimeField(auto_now_add=True)