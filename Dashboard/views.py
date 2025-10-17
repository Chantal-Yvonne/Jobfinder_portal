from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobForm
from .models import Job, Application
from employee.models import JobApplication
from django.core.paginator import Paginator


# This is to post a job
@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('dashboard:overview')  # This should match the URL name
    else:
        form = JobForm()
    return render(request, 'dashboard/post_job.html', {'form': form})

# Update a job
@login_required
def update_job(request, pk):
    job = get_object_or_404(Job, pk=pk, posted_by=request.user)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('dashboard:overview')
    else:
        form = JobForm(instance=job)
    return render(request, 'dashboard/update.html', {'form': form})

# @login_required
# def delete_job(request, pk):
#     job = get_object_or_404(Job, pk=pk, posted_by=request.user)

#     if request.method == 'POST':
#         job.delete()
#         return redirect('item:browse')  # Or wherever you want to go after deletion

#     return render(request, 'dashboard/confirm_delete.html', {'job': job})

# @login_required
# def delete_job(request, pk):
#     job = get_object_or_404(Job, pk=pk, posted_by=request.user)

#     if request.method == 'POST':
#         job.delete()
#         return redirect('dashboard:overview')  # Or wherever you want to go after deletion

#     # Optional: prevent GET request from deleting
#     return redirect('dashboard:overview')

# Delete a job
# @login_required
# def delete_job(request, pk):
#     job = get_object_or_404(Job, pk=pk, posted_by=request.user)
#     if request.method == 'POST':
#         job.delete()
#         return redirect('dashboard:overview')
#     return HttpResponseNotAllowed(['POST'])

@login_required
def delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk, posted_by=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('dashboard:overview')  # ✅ Correct redirect
    return HttpResponseNotAllowed(['POST'])


# View to see who applied to your posted jobs
@login_required
def view_applicants_to_my_jobs(request):
    jobs = Job.objects.filter(posted_by=request.user)
    applicants = JobApplication.objects.filter(job__in=my_jobs).select_related('job', 'job__posted_by')
    return render(request, 'dashboard/applicants.html', {'applicants': applicants})

# View to see which jobs the user applied to
@login_required
def jobs_user_applied_to(request):
    applications = Application.objects.filter(applicant=request.user).select_related('job')
    return render(request, 'dashboard/applied_jobs.html', {'applications': applications})

# Dashboard overview combining all tables
@login_required
def dashboard_overview(request):
    my_jobs = Job.objects.filter(posted_by=request.user)
    applicants = Application.objects.filter(job__in=my_jobs).select_related('job', 'applicant')
    applied_jobs = Application.objects.filter(applicant=request.user).select_related('job')

    context = {
        'my_jobs': my_jobs,
        'applicants': applicants,
        'applied_jobs': applied_jobs,
    }
    return render(request, 'dashboard/overview.html', context)

# New: Delete an application the user made
@login_required
def delete_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, applicant=request.user)
    if request.method == 'POST':
        application.delete()
        return redirect('dashboard:overview')
    return HttpResponseNotAllowed(['POST'])


def job_listings(request):
    jobs_list = Job.objects.all().order_by('-date_posted')  # or your desired ordering
    paginator = Paginator(jobs_list, 6)  # Show 6 jobs per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard/job_listings.html', {'page_obj': page_obj})