from django import forms 
from .models import JobApplication

# class EmployeeForm(forms.ModelForm):
#     # created nested class called meta 
#     class Meta:
#         model = Employee
#         # 2 ways to write fields for each field in model , in tuple etc you do this when you want specific fields in your model - but in this case we require all fields based on structure : this retrieves all fields for the form 
#         fields = '__all__'


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ('job', 'applicant', 'created_at')  
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'motivational': forms.Textarea(attrs={'class': 'form-control', 'rows':4}),
            'curriculum_vitae': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_curriculum_vitae(self):
        cv = self.cleaned_data.get('curriculum_vitae')
        if cv:
            if cv.size > 5*1024*1024:
                raise forms.ValidationError("CV file too large (max 5MB).")
            if not cv.name.endswith(('.pdf', '.doc', '.docx')):
                raise forms.ValidationError("CV must be a PDF or Word document.")
        return cv



