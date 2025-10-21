from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator




class Job(models.Model):
    """model for job """
    
    JOB_CATEGORIES = [
    ('Healthcare','Healthcare'),
    ('Education','Education'),
    ('IT & Software','IT & Software'),
]

    JOB_NATURE_CHOICES = [
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
        ('Remote','Remote'),
        ('Freelance','Freelance'),
    ]

    # Basic job info
    category = models.CharField(max_length=50, choices=JOB_CATEGORIES, blank=True, null=True)
    job_position = models.CharField(max_length=255)
    description = models.TextField(max_length=600)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateField(auto_now_add=True)
    company_name = models.CharField(max_length=255)

    # # Dropdowns
    # category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    # job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES, default='full-time')

    # Additional fields needed for template
    city_location = models.CharField(max_length=255, blank=True, null=True)
    vacancy = models.PositiveIntegerField(default=1)
    job_nature = models.CharField(max_length=20,choices=JOB_NATURE_CHOICES, blank=True, null=True)
    # yearly_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    application_deadline = models.DateField(blank=True, null=True)

    # Company info
    company_description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)
    # image = models.ImageField(upload_to='cvs/', blank=True, null=True)

    # Skills and experience lists for template loops
    skills = models.TextField(blank=True, null=True, help_text ="Comma-seperated list of skills")
    experience = models.TextField(blank=True, null=True, help_text ="Comma-seperated list of skills")

    # Relations
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True)
    
    #track if the job has been taken
    is_filled = models.BooleanField(default=False)



    def __str__(self):
        return f"{self.job_position} at {self.company_name}"
    
    def skills_list(self):
        if self.skills:
            return [skill.strip() for skill in self.skills.split(',')]
        return []
        
    def experience_list(self):
        if self.experience:
            return [exp.strip() for exp in self.experience.split(',')]
        return []

    
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    cv = models.FileField(
        upload_to='cvs/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]
    )
    date_applied = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'applicant')  # Prevent duplicate applications

    def __str__(self):
        return f"{self.applicant.username} applied to {self.job}"
