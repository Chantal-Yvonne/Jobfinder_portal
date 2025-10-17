from django.db import models
from Dashboard.models import Job
from django.contrib.auth.models import User
# Create your models here.
# class Employee(models.Model):
#     employee_id = models.CharField(max_length=20)
#     employee_name = models.CharField(max_length=100)
#     employee_email = models.EmailField()
#     employee_contact = models.CharField(max_length=20)

#     def __str__(self):
#         return self.employee_name




class JobApplication(models.Model):
    job = models.ForeignKey('Dashboard.Job', on_delete=models.CASCADE, related_name='employee_applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)  # stores logged-in user
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    motivational = models.TextField(blank=True, null=True)
    curriculum_vitae = models.FileField(upload_to='cvs/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'applicant')  # prevent duplicate applications

    def __str__(self):
        return f"{self.full_name} applied to {self.job}"
