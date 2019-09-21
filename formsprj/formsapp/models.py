from django.db import models


# Create your models here.

class Employee(models.Model):
    empname = models.CharField(max_length=100)
    salary = models.IntegerField()
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.empname
