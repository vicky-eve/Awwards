from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from awardapp.models import Project, Profile

# Create your views here.
@login_required(login_url='/registration/login/')
def index(request):
    """
    display all projects and profiles
    """
    projects = Project.objects.all
    profiles = Profile.objects.all

    return render(request, 'index.html', {'projects':projects, 'profiles':profiles})

