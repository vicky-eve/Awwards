from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.TextField(max_length=50)
    landingpage_pic = models.ImageField(upload_to=('images/'), null=True)
    description = models.TextField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True,blank=True)
    link = models.URLField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project')

class Profile(models.Model):
    username = models.TextField(max_length=50, blank=True)
    bio = models.TextField(max_length=200, blank=True)
    contact_info = models.IntegerField(max_length=11)
    profile_pic = models.ImageField(upload_to=('images/'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

class Review(models.Model):
    usability = models.IntegerField()
    design = models.IntegerField()
    creativity = models.IntegerField()
    content = models.IntegerField
    developer = models.IntegerField()