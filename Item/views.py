from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from Dashboard.models import Job, Application
from django.urls import reverse
from Dashboard.models import Job


@login_required
def browse_jobs(request):
    jobs = Job.objects.all()

    position = request.GET.get('position')
    company = request.GET.get('company')
    category = request.GET.get('category')
    job_type = request.GET.get('job_type')

    if position:
        jobs = jobs.filter(job_position__icontains=position)
    if company:
        jobs = jobs.filter(company_name__icontains=company)
    if category:
        jobs = jobs.filter(category=category)
    if job_type:
        jobs = jobs.filter(job_type=job_type)

    user_applications = Application.objects.filter(applicant=request.user)
    applied_job_ids = user_applications.values_list('job_id', flat=True)

    context = {
        'jobs': jobs,
        'applied_job_ids': applied_job_ids,
        'position_filter': position or '',
        'company_filter': company or '',
        'category_filter': category or '',
        'job_type_filter': job_type or '',
        'categories': Job.CATEGORY_CHOICES,
        'job_types': Job.JOB_TYPE_CHOICES,
    }
    return render(request, 'browse.html', context)


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)

    user_is_owner = request.user == job.posted_by if request.user.is_authenticated else False
    user_has_applied = False

    if request.user.is_authenticated and not user_is_owner:
        user_has_applied = Application.objects.filter(applicant=request.user, job=job).exists()

    context = {
        'job': job,
        'user_is_owner': user_is_owner,
        'user_has_applied': user_has_applied,
    }
    return render(request, 'job_detail.html', context)


@login_required
def apply_to_job(request, pk):
    # Redirect to dashboard app's apply view
    return redirect(reverse('dashboard:apply', kwargs={'pk': pk}))


@login_required
def edit_job(request, pk):
    # Redirect to dashboard's edit job view
    return redirect(reverse('dashboard:update', kwargs={'pk': pk}))


@login_required
def delete_job(request, pk):
    # Redirect to dashboard's delete job view
    return redirect(reverse('dashboard:delete', kwargs={'pk': pk}))


@login_required
def delete_application(request, pk):
    application = get_object_or_404(Application, pk=pk, applicant=request.user)
    job_id = application.job.id  # Store job id for redirect
    application.delete()
    # Redirect back to the job detail page after deletion
    return redirect(reverse('item:detail', kwargs={'pk': job_id}))


