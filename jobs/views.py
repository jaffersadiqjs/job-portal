from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Job
from .forms import ApplicantForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def job_list(request):
    jobs = Job.objects.all().order_by('-posted_date')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.job = job
            app.save()
            messages.success(request, "Application submitted successfully!")
            return redirect('job_list')
    else:
        form = ApplicantForm()
    return render(request, 'jobs/job_detail.html', {'job': job, 'form': form})
