from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2= request.POST['password2']
        email=request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is already taken')
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, ' This email address is already use')
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.is_active=False
                user.save()
                subject='welcome to Brandless Private Limited'
                message=f'Hi {user.first_name} {user.last_name}, thank you for registering in Brandless'
                email_from=settings.EMAIL_HOST_USER
                recipient_list=[user.email]
                send_mail(subject, message, email_from, recipient_list)
                return redirect("login")
        else:
            messages.info(request, 'password is mismatch')
            return redirect("register")
    else:
        return render(request, 'register2.html')


def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"username or password is  incorrect!!!")
            return redirect("login")
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")





