from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('search/', views.search_project, name='search_project'),
    path('post_project/', views.post_project, name='post_project'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('profile/', views.profile, name='profile'),
    path('review/<int:project_id>/', views.review, name='review'),
    path('accounts/profile/', views.profile, name='profile'),
    path('api/project/', views.ProjectList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/review/', views.ReviewList.as_view()),
    path('api/merch/project-id/(?P<pk>[0-9]+)/',views.ProjectDescription.as_view()),
    path('api/merch/profile-id/(?P<pk>[0-9]+)/',views.ProfileDescription.as_view()),
    path('api/merch/review-id/(?P<pk>[0-9]+)/',views.ReviewDescription.as_view()),
   
]