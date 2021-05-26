from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.registerUser),
    path('logout', views.logout),
    path('login', views.login),
    path('quotes', views.quotes),
    path('quotes/addquote', views.create)
]