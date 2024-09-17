from django.db import models

# Create your models here.
class Employeedetails(models.Model):
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    hiredate=models.DateField()

