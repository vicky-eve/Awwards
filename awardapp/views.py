from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from awardapp.models import Project, Profile, Review, User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer, ReviewSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.http import Http404
from.forms import RegistrationForm, UploadProjectForm, UpdateProfileForm, ProjectForm
from django.contrib import messages


#api views
class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)
        

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewList(APIView):
    def get(self, request, format=None):
        all_reviews = Review.objects.all()
        serializers = ReviewSerializer(all_reviews, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ReviewSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

    

class ReviewDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_review(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        review = self.get_review(pk)
        serializers = ReviewSerializer(review)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        review = self.get_review(pk)
        serializers = ReviewSerializer(review, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        review = self.get_review(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.

def index(request):
    """
    display all projects and profiles
    """
    projects = Project.objects.all
   

    return render(request, 'index.html', {'projects':projects})

@login_required(login_url='/registration/register/')
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'{username} you have successfully created your account')
            return redirect ('login')
    else:
        form=RegistrationForm()
        return render (request, 'registration/registration_form.html', {"form":form})



@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, "registration/profile.html", {"profile": profile, })



def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    return render(request, 'registration/update_profile.html', {"form":form, "profile":profile, 'id':id})  

@login_required(login_url='/accounts/login/')
def post_project(request):
    projects = Project.objects.all().order_by('-id')
    if request.method == 'POST':  
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            commit = form.save(commit=False)
            commit.user = request.user
            commit.save()
            return redirect('index')
    
    else:
        form = ProjectForm() 
    return render (request, 'post.html', {'form':form, 'projects':projects})

@login_required(login_url='/accounts/login/')
def search_project(request):    
    if 'search' in request.GET and request.GET['search']:        
        search_term = request.GET.get('search').lower()        
        images = Project.search_project_title(search_term)        
        message = f'{search_term}'
        return render(request, 'search.html', {'found': message, 'images': images})    
    else:       
         message = 'Not found'        
    return render(request, 'search.html', {'danger': message})

def project(request, project_id):
    projects = Project.objects.get(id=project_id)
    return render(request, "review.html", {"projects": projects})

@login_required(login_url='/accounts/login/')
def review(request,project_id):
    if request.method == 'POST':
        project= Project.objects.get(id = project_id)
        current_user = request.user
        usability = request.POST['usability']
        design = request.POST['design']
        creativity= request.POST['creativity']
        content = request.POST['content']
        developer = request.POST['developer']

        Review.objects.create(
            project=project,
            user=current_user,
            usability=usability,
            design=design,
            content=content,
            creativity=creativity,
            developer=developer,
            average=round((float(design)+float(usability)+float(content)+float(developer)+float(creativity))/5,2),)

        return render(request,'review.html',{'project':project})
    else:
        project = Project.objects.get(id = project_id) 
        return render(request,'review.html',{'project':project})