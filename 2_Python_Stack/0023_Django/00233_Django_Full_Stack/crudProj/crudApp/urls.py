from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_form', views.process_form),
    path('edit_bday/<int:bday_id>', views.edit_bday),
    path('process_edit/<int:bday_id>', views.process_edit)
]