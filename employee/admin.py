from django.contrib import admin
from django.utils.html import format_html
from .models import JobApplication  # import your model
# Register your models here.
# employee/admin.py


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'job','motivational', 'curriculum_vitae_link', 'created_at')

    def curriculum_vitae_link(self, obj):
        if obj.curriculum_vitae:
            return format_html('<a href="{}" target="_blank">View CV</a>', obj.curriculum_vitae.url)
        return "-"
    curriculum_vitae_link.short_description = "CV"

# Register the model with the custom admin
admin.site.register(JobApplication, JobApplicationAdmin)
