# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('major/', views.major_index),
    path('major/edit/', views.major_edit),
    path('student/', views.student_index),
    path('student/add/', views.student_add),
    path('student/edit/', views.student_edit),
    path('student/delete/', views.student_delete),
    path('course/', views.course_index),
    path('award/', views.award_index),
    path('sa/', views.sa_index),
    path('sa/add/', views.sa_add),
    path('sa/delete/', views.sa_delete),
    path('sc/', views.sc_index),
    path('sc/add/', views.sc_add),
    path('sc/edit/', views.sc_edit),
    path('sc/delete/', views.sc_delete)
]
