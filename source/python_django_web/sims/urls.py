# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('student/', views.student_index),
    path('major/', views.major_index)
]
