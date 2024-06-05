# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('major/', views.major_index),
    path('student/', views.student_index),
    path('course/', views.course_index)
]
