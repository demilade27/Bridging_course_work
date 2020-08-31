from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('resume/', views.resume, name='resume'),
    path('resume/add_resume', views.add_resume, name='add_resume'),
    path('resume/<int:pk>/edit/', views.edit_resume, name='edit_resume'),
]