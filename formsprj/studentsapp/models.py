from django.db import models


# Create your models here.
class StudentModel(models.Model):
    Name = models.CharField(max_length=50)
    Course = models.CharField(max_length=50)
    Admission_No = models.IntegerField()

    def __str__(self):
        return self.Name
