# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('major/', views.major_index),
    path('major/edit', views.major_edit),
    path('student/', views.student_index),
    path('student/add', views.student_add),
    path('student/delete', views.student_delete),
    path('course/', views.course_index) 
]
