from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.browse_jobs, name='browse'),                 # List jobs
    path('<int:pk>/', views.job_detail, name='detail'),         # Job detail
    path('<int:pk>/apply/', views.apply_to_job, name='apply'), # Apply to job
    path('job/edit/<int:pk>/', views.edit_job, name='edit_job'), #edit the job
    path('job/delete/<int:pk>/', views.delete_job, name='delete_job'), #delete the job
    path('application/<int:pk>/delete/', views.delete_application, name='delete_application'),  # Delete an application
]
