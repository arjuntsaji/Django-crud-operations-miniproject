from django.shortcuts import render,redirect,get_object_or_404
from .models import Employees
from .form import EmployeeForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

# Create your views here.


def home(request):
    return render(request,"index.html")


def employeeform(request,id=0):
    if request.method=="GET":
        if id == 0:
            form=EmployeeForm()
        else:
            employee=Employees.objects.get(id=id)
            form=EmployeeForm(instance=employee)
        return render(request,"employee_form.html",{'form':form})
    else:
        if id == 0 :
            form=EmployeeForm(request.POST,request.FILES)

        else:
            employee=Employees.objects.get(id=id)
            form=EmployeeForm(request.POST,request.FILES,instance=employee)

        if form.is_valid():
            form.save()
            return redirect("employee_list")


def employeelist(request):
    employees=Employees.objects.all()
    return render(request,'employee_list.html',{'employees':employees})


def delete(request,id):
    employee=Employees.objects.get(id=id)
    if request.method=='POST':
        employee.delete()
        return redirect("/employeelist")
    return render(request,'delete_confirm.html')
























