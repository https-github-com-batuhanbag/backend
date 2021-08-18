from django.contrib import admin
from django.urls import path
from . import views
app_name = "userprofile"

urlpatterns = [


    path('register/', views.registration_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('userupdate/', views.user_view, name="userupdate"),


]
