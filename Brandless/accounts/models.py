from django.db import models
# from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.


class Position(models.Model):
    title=models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Department(models.Model):
    department=models.CharField(max_length=30)

    def __str__(self):
        return self.department


class Typeofwork(models.Model):
    type=models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Employees(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    emp_id = models.CharField(max_length=30)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    email= models.EmailField(max_length=30)
    number = models.BigIntegerField()
    position = models.ForeignKey(Position,on_delete=models.SET_NULL,null=True)
    typeofwork = models.ForeignKey(Typeofwork,on_delete=models.SET_NULL,null=True)
    resume_file=models.FileField(null=True,upload_to='resume',blank=True)

    def __str__(self):
        return self.first_name

