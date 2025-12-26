from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),


    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path("student/", views.register_student, name="student"),
    path('students/', views.view_student, name='student_list'),
    path('student/update/<int:id>/', views.update_student, name='update_student'),
    path('student/delete/<int:id>/', views.delete_student, name='delete_student'),


    
]
