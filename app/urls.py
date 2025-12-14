from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('create/', views.create_resume, name='create_resume'),
    path('<int:resume_id>/', views.resume_detail, name='resume_detail'),
    path('<int:resume_id>/add-skill/', views.add_skill, name='add_skill'),
    path('<int:resume_id>/add-experience/', views.add_experience, name='add_experience'),
    path('<int:resume_id>/add-education/', views.add_education, name='add_education'),
]
