from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, Application

def home(request):
    jobs = Job.objects.all()
    return render(request, 'home.html', {'jobs': jobs})


@login_required
def post_job(request):
    if request.method == 'POST':
        Job.objects.create(
            employer=request.user,
            title=request.POST['title'],
            description=request.POST['description'],
            location=request.POST['location']
        )
        return redirect('home')
    return render(request, 'post_job.html')


@login_required
def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        Application.objects.create(
            job=job,
            applicant=request.user,
            resume=request.FILES['resume']
        )
        return redirect('home')
    return render(request, 'apply_job.html', {'job': job})
