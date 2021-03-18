from django.contrib import admin
from accounts.models import Employees,Department,Position,Typeofwork

# Register your models here.
admin.site.register(Employees)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Typeofwork)

