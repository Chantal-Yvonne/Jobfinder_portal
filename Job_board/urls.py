"""
URL configuration for Job_board project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Can be thought of as a table of contents for the whole project , link url to specific view 
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# import views from apps 
urlpatterns = [
    path('admin/', admin.site.urls),
    #all urls that begin with item/ will automatically go into item.urls
    path('jobs_and_applications/', include(('Dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('item/', include('Item.urls')),
    path('', include('Home.urls')),
    path('applicant/', include('employee.urls', namespace='employee')),
    path('', include('Dashboard.urls')),  # make jobs available at /jobs/
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)