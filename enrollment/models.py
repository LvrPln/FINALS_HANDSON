from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    units = models.PositiveSmallIntegerField(default=3)

class Department(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    head = models.CharField(max_length=200, blank=True)

class StudentProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=50)
    birthdate = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=300, blank=True)
    contact = models.CharField(max_length=50, blank=True)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=200)
    paid_on = models.DateTimeField(auto_now_add=True)
