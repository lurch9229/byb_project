from django.urls import path
from . import views

# Added urls for adding, editing, deleting and toggling visiblity
urlpatterns = [
    # Define your app-specific paths here
    path('', views.index, name='index'),
    path('add/', views.add_note, name='add_note'),
    path('edit/<int:pk>/', views.edit_note, name='edit_note'),
    path('update/<int:pk>/', views.update_note, name='update_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('toggle/<int:note_id>/', views.toggle_note, name='toggle_note'),
]
