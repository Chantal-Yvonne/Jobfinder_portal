from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_overview, name='overview'),  # dashboard homepage with all tables
    path('create/', views.post_job, name='create'),
    path('delete/<int:pk>/', views.delete_job, name='delete'),
    path('update/<int:pk>/', views.update_job, name='update'),
    path('applicants/', views.view_applicants_to_my_jobs, name='applicants'),  # optional
    path('applied/', views.jobs_user_applied_to, name='applied'),             # optional
    path('application/delete/<int:pk>/', views.delete_application, name='delete_application'),  # delete user's application
    path('jobs/', views.job_listings, name='job_listings'),
]
