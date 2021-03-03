from django.urls import path
from . import views

urlpatterns = [
    path('start_job', views.start_job)
]