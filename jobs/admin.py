from django.contrib import admin
from .models import Job, Applicant

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_date')
    search_fields = ('title', 'company', 'location')

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job', 'applied_date')
    list_filter = ('job',)
