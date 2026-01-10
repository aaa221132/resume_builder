"""
URL configuration for project project.

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
from django.contrib import admin
from django.urls import include, path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),

    path('', views.resume_list, name='home'),
    path('', views.resume_list, name='resume_list'),
    
    path('create/', views.create_resume, name='create_resume'),
    path('<int:resume_id>/', views.resume_detail, name='resume_detail'),
    path('<int:resume_id>/add-skill/', views.add_skill, name='add_skill'),
    path('<int:resume_id>/add-experience/', views.add_experience, name='add_experience'),
    path('<int:resume_id>/add-education/', views.add_education, name='add_education'),
]
