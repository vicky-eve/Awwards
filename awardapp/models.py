from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.TextField(max_length=50)
    landingpage_pic = models.ImageField(upload_to=('images/'), null=True)
    description = models.TextField(max_length=200)

class Profile(models.Model):
    username = models.TextField(max_length=50)
    bio = models.TextField(max_length=200)
    contact_info = models.IntegerField(max_length=11)
    profile_pic = models.ImageField(upload_to=('images/'))
    
