from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.registerUser),
    path('home', views.home),
    path('logout', views.logout),
    path('login', views.login)
]