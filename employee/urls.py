from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('apply/<int:pk>/', views.apply, name='apply'), #apply for the job
    path('edit/<int:pk>/', views.edit_application, name='edit_application'), #edit application
    path('delete/<int:pk>/', views.delete_application, name='delete_application'), #delete application
    path('dashboard/', views.dashboard, name='dashboard'), #view the employee dashboard
]
