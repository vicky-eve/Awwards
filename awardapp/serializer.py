from rest_framework import serializers
from .models import Profile, Project, Review

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'landingpage_pic', 'description', 'link')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'bio', 'contact_info', 'profile_pic')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('usability', 'design', 'creativity', 'content', 'developer')