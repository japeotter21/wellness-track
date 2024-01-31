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
    drankAt = models.DateTimeField(default="2024-01-27T05:02:06.387082Z")
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

class Mood(models.Model):
    mood = models.TextField(choices=[("S", "Sleepy"),("T","Tired"),("W","Awake"),("A","Alert")])
    time = models.DateTimeField(auto_now_add=True)
    
class Focus(models.Model):
    focus = models.IntegerField(default=1)
    time = models.DateTimeField(auto_now_add=True)

class ScreenTime(models.Model):
    hours = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)