from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('create/', views.create_resume, name='create_resume'),
    path('<int:resume_id>/', views.resume_detail, name='resume_detail'),
    path('<int:resume_id>/delete/', views.delete_resume, name='delete_resume'),
    

    path('<int:resume_id>/add-skill/', views.add_skill, name='add_skill'),
    path('skill/<int:skill_id>/delete/', views.delete_skill, name='delete_skill'),

    path('<int:resume_id>/add-experience/', views.add_experience, name='add_experience'),
    path('experience/<int:exp_id>/delete/', views.delete_experience, name='delete_experience'),

    path('<int:resume_id>/add-education/', views.add_education, name='add_education'),
    path('education/<int:edu_id>/delete/', views.delete_education, name='delete_education'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
