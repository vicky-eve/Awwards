from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('^api/project/$', views.ProjectList.as_view()),
    path('^api/profile/$', views.ProfileList.as_view()),
    path('^api/review/$', views.ReviewList.as_view()),
]