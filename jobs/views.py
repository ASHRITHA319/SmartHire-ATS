from django.shortcuts import render
from .models import Job
from applications.models import Application
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def job_list(request):

    jobs = Job.objects.all()

    query = request.GET.get('q')

    if query:

        jobs = jobs.filter(
            title__icontains=query
        ) | jobs.filter(
            company__icontains=query
        )

    applied_jobs = []

    if request.user.is_authenticated:

        applied_jobs = Application.objects.filter(
            applicant=request.user
        ).values_list('job_id', flat=True)

    context = {
        'jobs': jobs,
        'applied_jobs': applied_jobs
    }

    return render(request, 'jobs/job_list.html', context)

@login_required(login_url='/accounts/login/')
def apply_job(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    already_applied = Application.objects.filter(
        applicant=request.user,
        job=job
    ).exists()

    if not already_applied:
        Application.objects.create(
            applicant=request.user,
            job=job
        )

    return redirect('/jobs/')

@login_required(login_url='/accounts/login/')
def my_applications(request):

    applications = Application.objects.filter(
        applicant=request.user
    )

    return render(
        request,
        'jobs/my_applications.html',
        {'applications': applications}
    )

@login_required(login_url='/accounts/login/')
def manage_applications(request):

    if not request.user.is_superuser:
        return HttpResponseForbidden("Access Denied")

    applications = Application.objects.all()

    return render(
        request,
        'jobs/manage_applications.html',
        {'applications': applications}
    )


@login_required(login_url='/accounts/login/')
def update_status(request, application_id):

    if not request.user.is_superuser:
        return HttpResponseForbidden("Access Denied")

    application = get_object_or_404(
        Application,
        id=application_id
    )

    if request.method == 'POST':

        new_status = request.POST['status']

        application.status = new_status

        application.save()

    return redirect('/jobs/manage-applications/')