from django.db import models

# Create your models here.


class Departments(models.Model):
    department=models.CharField(max_length=30)

    def __str__(self):
        return self.department


class Complaint_form(models.Model):
    full_name=models.CharField(max_length=30)
    emp_id=models.CharField(max_length=30)
    department=models.ForeignKey(Departments,on_delete=models.SET_NULL,null=True)
    number=models.BigIntegerField()
    complaint=models.CharField(max_length=200)