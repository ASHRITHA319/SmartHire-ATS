from django.urls import path
from .views import job_api

urlpatterns = [

    path('jobs/', job_api),
]