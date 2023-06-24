from django.db import models
# Create your models here.
from django.db import models
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext_lazy as _
from users.models import User

class privacy(models.Model):
    PRIVACY = [("friends", "Friends"), ("public", "Public")]
    name = models.CharField(max_length=200, choices=PRIVACY)
    policy = models.CharField(max_length=200, default='Posted property is owned by the posted user')

# Create your models here.
class Property(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    rooms = models.IntegerField(blank=True,editable=False, null=True)
    baths = models.CharField(blank=True,editable=False, max_length=200, null=True)
    area = models.CharField(blank=True,editable=False, max_length=200, null=True)
    price = models.IntegerField(blank=True,editable=False, null=True)
    title = models.CharField(blank=True,editable=False, max_length=200, null=True)
    coverPhoto = models.ImageField(blank=True, upload_to="properties/passports/")
    photos = models.ImageField(blank=True, upload_to="properties/passports/")
    state = models.CharField(blank=True,editable=False, max_length=200, null=True)
    rentType = models.CharField(blank=True,editable=False, max_length=200, null=True)
    description = models.CharField(blank=True,editable=False, max_length=200)
    privacy = models.ForeignKey(privacy,on_delete=models.CASCADE)
    

class Comment(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    total_comments = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.total_comments = 0
    #     super().save(*args, **kwargs)
    
    # def increase_comments(self):
    #     self.total_comments += 1
    #     self.save()


class Reactions(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    flags = models.IntegerField(default=0)

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.total_comments = 0
    #     super().save(*args, **kwargs)
    
    # def increase_comments(self):
    #     self.total_comments += 1
    #     self.save()


