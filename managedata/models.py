from django.db import models

# Create your models here.

class Employee(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]   

    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    appointment_date = models.DateField()

    def __str__(self):
        return self.name

