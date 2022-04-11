from email.mime import image
from django import forms
from .models import User, Profile, Project
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    class Meta:
        model = User
        fields=['username', 'email', 'password1', 'password2']
        help_texts = {'username':None, 'password2':None}
User._meta.get_field('email')._unique = True

class UploadProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'landingpage_pic', 'description', 'link' ]

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=( 'username', 'bio', 'contact_info', 'profile_pic')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields =('title', 'landingpage_pic', 'description', 'link')

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    
    
    class Meta:
        model = User
        fields=['username', 'email', 'password1', 'password2']
        help_texts = {'username':None, 'password2':None}
User._meta.get_field('email')._unique = True