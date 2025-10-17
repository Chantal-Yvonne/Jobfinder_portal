from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('apply/<int:pk>/', views.apply, name='apply'),
    path('edit/<int:pk>/', views.edit_application, name='edit_application'),
    path('delete/<int:pk>/', views.delete_application, name='delete_application'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
