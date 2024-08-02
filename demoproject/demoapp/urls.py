from . import views
from django.urls import path

urlpatterns=[
    path('studentapi/', views.student_api),
]