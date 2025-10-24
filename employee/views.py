from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from .forms import JobApplicationForm
from Dashboard.models import Job
from .models import JobApplication


# View: Apply for a job
@login_required
def apply(request, pk):
    job = get_object_or_404(Job, id=pk)

    # Check if the user already applied
    if JobApplication.objects.filter(job=job, applicant=request.user).exists():
        messages.error(request, "You have already applied for this job.")
        return redirect('employee:dashboard')  # or another page

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, "Your application has been submitted successfully.")
            return redirect('employee:dashboard')
    else:
        form = JobApplicationForm()

    return render(request, 'employee/application_form.html', {'form': form, 'job': job})


# View: Edit an existing job application
@login_required
def edit_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, applicant=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application updated successfully!')
            return redirect('dashboard:overview')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        form = JobApplicationForm(instance=application)

    return render(request, 'employee/application_form.html', {'form': form, 'title': 'Edit Application'})


# View: Delete (withdraw) a job application
@login_required
def delete_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, applicant=request.user)
    if request.method == 'POST':
        application.delete()
        messages.success(request, 'Application withdrawn successfully!')
        return redirect('dashboard:overview')
    return HttpResponseNotAllowed(['POST'])


# employee/views.py
@login_required
def dashboard(request):
    user = request.user

    # Jobs posted by the user (assuming Job has a `posted_by` field)
    my_jobs = Job.objects.filter(posted_by=user)

    # Applicants to jobs posted by this user
    applicants = JobApplication.objects.filter(job__in=my_jobs)

    # Jobs the user has applied to
    applied_jobs = JobApplication.objects.filter(applicant=user)

    context = {
        'my_jobs': my_jobs,
        'applicants': applicants,
        'applied_jobs': applied_jobs,
    }
    return render(request, 'dashboard/overview.html', context)
