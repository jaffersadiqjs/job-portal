from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    company = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Applicant(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} -> {self.job.title}"
