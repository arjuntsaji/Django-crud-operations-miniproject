from django.shortcuts import render,redirect
from .form import ComplaintForm

# Create your views here.


def complaint(request):
    if request.method == 'POST':
        form=ComplaintForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form=ComplaintForm
        return render(request,'complaint_form.html',{'form':form})
