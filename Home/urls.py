from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),                     # Home page
    path('signup/', views.signup, name='signup'),            # Signup page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(next_page='home:index'), name='logout'),  # Logout, redirects to home
    path('about/', views.about, name='about'),                # About page

    # Redirects to dashboard for post and dashboard overview
    path('post/', views.post, name='post'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
