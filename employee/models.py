from django.db import models
from Dashboard.models import Job
from django.contrib.auth.models import User
# Create your models here.




class JobApplication(models.Model):
    """The job this application is linked to.If the job is deleted, all related applications are also deleted (CASCADE)."""
    job = models.ForeignKey('Dashboard.Job', on_delete=models.CASCADE, related_name='employee_applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)  # many-to-one relationship.Links a job application to the user who applied.
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
