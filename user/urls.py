from django.contrib import admin
from django.urls import include, path
from user import views
from django.contrib.auth import views as authentication_views


urlpatterns = [
    path('login/', authentication_views.LoginView.as_view(template_name = "user/login.html"), name = "login"), 
    path('logout/', authentication_views.LogoutView.as_view(template_name = "user/logout.html"), name = "logout"), 
    path('profile/', authentication_views.profilePage, name = "profilePage"),
]
