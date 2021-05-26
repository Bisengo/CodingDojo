from django.urls import path
from . import views

urlpatterns = [
    path('', views.show),
    path('shows', views.show),
    path('shows/new', views.newForm),
    path('shows/create', views.process_form),
    path('shows/<int:show_id>', views.showInfo),
    path('shows/<int:show_id>/edit', views.editShow),
    path('shows/<int:show_id>/update', views.updateShow),
    path('shows/<int:show_id>/destroy', views.delete)
]
