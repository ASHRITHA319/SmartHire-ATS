from django.urls import path

from .views import (
    job_list,
    apply_job,
    my_applications,
    manage_applications,
    update_status
)

urlpatterns = [

    path('', job_list, name='job_list'),

    path('apply/<int:job_id>/', apply_job, name='apply_job'),

    path('my-applications/', my_applications, name='my_applications'),

    path('manage-applications/',manage_applications,name='manage_applications'),

    path('update-status/<int:application_id>/',update_status,name='update_status'),
]