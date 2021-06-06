from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('activate/<uidb64>/<token>/', views.activate, name="activate"),
    path('email_verification', views.token_sent, name="email_verification"),
    path('token_fail', views.fail, name="token_fail"),
    path('token_success', views.token_success, name="token_success"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="reset_password.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
    path('validate_username',views.validate_username,name="validate_username")
]
