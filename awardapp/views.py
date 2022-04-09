from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from awardapp.models import Project, Profile, Review
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer, ReviewSerializer

#api views
class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class ReviewList(APIView):
    def get(self, request, format=None):
        all_reviews = Review.objects.all()
        serializers = ReviewSerializer(all_reviews, many=True)
        return Response(serializers.data)

# Create your views here.
@login_required(login_url='/registration/login/')
def index(request):
    """
    display all projects and profiles
    """
    projects = Project.objects.all
    profiles = Profile.objects.all

    return render(request, 'index.html', {'projects':projects, 'profiles':profiles})

