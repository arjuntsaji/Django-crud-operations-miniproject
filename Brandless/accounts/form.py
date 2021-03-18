from django import forms
from accounts.models import Employees


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields = "__all__"
        labels={
            "first_name":"First Name",
            "last_name": "Last Name",
            "emp_id": "Emp Id",
            "typeofwork":"Type of Work",
            "position":"Position Level",
            "resume_file":"Upload Resume"
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args,**kwargs)
        self.fields["position"].empty_label = "Select"
        self.fields["department"].empty_label = "Select"
        self.fields["typeofwork"].empty_label = "Select"









