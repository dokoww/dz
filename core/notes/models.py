from django.db import models


# Create your models here.
class Note(models.Model):
    Dayoftheweek = models.CharField(max_length=20)
    descriptionoftheday = models.TextField(max_length=123)
    date = models.DateField()
