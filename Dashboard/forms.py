from django import forms
from .models import Job, Application

from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'job_position', 'company_name', 'description', 'salary',
            'city_location', 'vacancy', 'job_nature', 'application_deadline',
            'company_description', 'website', 'company_email', 'image', 'skills', 'experience'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Job Description'}),
            'company_description': forms.Textarea(attrs={'placeholder': 'Company Description'}),
            'application_deadline': forms.DateInput(attrs={'type': 'date'}),
            # 'posted_by': forms.DateInput(attrs={'type': 'date'}),
            'skills': forms.Textarea(attrs={'placeholder': 'Enter skills separated by commas'}),
            'experience': forms.Textarea(attrs={'placeholder': 'Enter experiences separated by commas'}),
        }

        
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['first_name', 'last_name', 'email', 'cv']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }
