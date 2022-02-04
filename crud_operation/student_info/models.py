from django.db import models
from django.contrib import admin

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100)
    std = models.CharField(max_length=10)
    sec = models.CharField(max_length=1)
    def __str__(self):
        return self.name
