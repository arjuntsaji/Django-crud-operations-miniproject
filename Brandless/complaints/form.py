from django import forms
from complaints.models import Complaint_form


class ComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint_form
        fields = "__all__"
        labels={
            "full_name":"Full Name",
            "emp_id":"Emp Id",
            "department":"Department",
            "number":"Mobile Number",
            "complaint":"Complaint Reason"
        }

    def __init__(self, *args, **kwargs):
        super(ComplaintForm, self).__init__(*args, **kwargs)
        self.fields["department"].empty_label = "Select"