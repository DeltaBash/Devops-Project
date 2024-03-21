"""
URL configuration for musicproj project.

This module defines the URL patterns for the musicproj project.
It includes routes for admin panel, user authentication, and user profiles.

For more information, refer to the Django documentation on URL routing:
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lyricapp.urls')),
    path('register/', user_views.register, name="user-register"),
    path('login/',
         auth_views.LoginView.as_view(template_name="users/login.html"),
         name="user-login"),
    path('logout/',
         auth_views.LogoutView.as_view(template_name="users/logout.html"),
         name="user-logout"),
    path('profile/', user_views.profile, name="user-profile"),
]
