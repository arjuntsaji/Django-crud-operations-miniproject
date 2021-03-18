from .import views
from django.urls import path


urlpatterns=[
    path('',views.home,name="homepage"),
    path('employeelist',views.employeelist,name="employee_list"),
    path('employeeform',views.employeeform,name="employee_insert"),
    path('edit/<str:id>/',views.employeeform,name="update_form"),
    path('delete/<str:id>/',views.delete,name="delete_form"),
   ]