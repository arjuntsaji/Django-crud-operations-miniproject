from django.urls import path
from .import views


urlpatterns=[
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('activate/<uidb64>/<token>/',views.activate,name="activate"),
    path('email_verification',views.token_sent,name="email_verification"),
    path('token_fail',views.fail,name="token_fail"),
    path('token_success',views.token_success,name="token_success")


]