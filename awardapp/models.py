from distutils.command.upload import upload
from phone_field import PhoneField
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
    title = models.TextField(max_length=50)
    landingpage_pic = CloudinaryField('images', null=True)
    description = models.TextField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True,blank=True)
    link = models.URLField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project')

    @classmethod
    def search_project(cls, user):
        return cls.objects.filter(user__username__icontains=user).all()

    def __str__(self):
        return f'{self.title}'

    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_projects(cls):
        return cls.objects.all()

    def save_project(self):
        self.save()

class Profile(models.Model):
    username = models.TextField(max_length=50, blank=True)
    bio = models.TextField(max_length=200, blank=True)
    contact_info = PhoneField(max_length=11, blank=True)
    profile_pic = CloudinaryField('images', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    @classmethod
    def search_profile(cls, user):
        return cls.objects.filter(user__username__icontains=user).all()


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username} Profile'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    usability = models.IntegerField(default=0,blank=True, null=True)
    design = models.IntegerField(default=0,blank=True, null=True)
    creativity = models.IntegerField(default=0,blank=True, null=True)
    content = models.IntegerField(default=0,blank=True, null=True)
    developer = models.IntegerField(default=0, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    average = models.IntegerField(default=0, blank=True, null=True)

    def save_review(self):
        self.save()

    @classmethod
    def get_review(cls, id):
        reviews = Review.objects.filter(project_id=id).all()
        return reviews

    def __str__(self):
        return self.user.username 
   