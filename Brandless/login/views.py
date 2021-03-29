from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.views.generic import View


# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

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
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                email_subject = 'Activate your account '
                message = render_to_string('activate.html', {

                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': generate_token.make_token(user)
                })
                email_message = EmailMessage(
                    email_subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [user.email]
                )

                email_message.send()
                return redirect("email_verification")
        else:
            messages.info(request, 'password is mismatch')
            return redirect("register")
    else:
        return render(request, 'register2.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "username or password is  incorrect!!!")
            return redirect("login")
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


def token_sent(request):
    return render(request, 'token_sent.html')


def token_success(request):
    return render(request, 'email_success.html')


def fail(request):
    return render(request, 'activate_failed.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError):
        user = None
    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        subject = 'welcome to Brandless Private Limited'
        message = f'Hi {user.first_name} {user.last_name}, Your account is successfully created.Now you can login'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('token_success')
    else:
        return redirect('token_fail')
