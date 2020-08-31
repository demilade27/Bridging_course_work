from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('aboutus/', views.about_us, name='about_us'),
    path('admin/', admin.site.urls, name='login_page'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
