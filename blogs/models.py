from django.db import models
# Create your models here.

class Blog(models.Model):
    title = models.CharField(blank=True,editable=False, max_length=200)
    published_date = models.DateTimeField(auto_created=True)
    link = models.CharField(blank=True,editable=False, max_length=200)
    
    