from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    summary = models.TextField()

class Reaction(models.Model):
    user_id = models.CharField(max_length=200)
    action = models.CharField(max_length=200)
    time = models.TimeField(auto_now=True)
    counts = models.IntegerField(default=0)