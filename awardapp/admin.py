from django.contrib import admin

from awardapp.models import Profile, Project, Review

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Review)