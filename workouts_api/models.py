from django.db import models
from django import forms
from datetime import datetime

# Create your models here.


class Workout(models.Model):
    date = models.DateField(("Date"), auto_now_add=True)
    exercises = models.CharField(max_length=50)
    notes = models.CharField(max_length=100)