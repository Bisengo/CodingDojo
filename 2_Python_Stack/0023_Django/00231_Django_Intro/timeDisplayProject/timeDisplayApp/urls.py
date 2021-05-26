from django.urls import path
from . import views

urlpatterns = [
    path('', views.display),
    path('time_display', views.display_td)
]