from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title