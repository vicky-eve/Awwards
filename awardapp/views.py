from django.shortcuts import render

from awardapp.models import Project, Profile

# Create your views here.
def index(request):
    """
    display all projects and profiles
    """
    projects = Project.objects.all
    profiles = Profile.objects.all

    return render(request, 'index.html', {'projects':projects, 'profiles':profiles})

