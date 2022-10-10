from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('comprehensive/', views.controlpage, name='controlpage'),
    path('teaching/', views.teachingform, name='teachingform'),
    path('planning/', views.planninglesson, name='planninglesson'),
    path('achievment/', views.educationachievment, name='achievment'),
    path('assessmenttome/', views.assessment_for_me, name='assessment_forme'),
    path('assessmentfromme/', views.assessment_from_me, name='assessment_fromme'),
]
