from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Shortlisted', 'Shortlisted'),
        ('Rejected', 'Rejected'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant.username
