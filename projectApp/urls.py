from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),

]
