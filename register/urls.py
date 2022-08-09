from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django_email_verification import urls as email_urls

urlpatterns = [

    path('',views.loginPage,name="login"),
    path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),
    path('verification/', views.verification, name="verification"),
    path('email/', include(email_urls)),

    path('reset_passwd/', 
    auth_views.PasswordResetView.as_view(template_name = 'register/passwd_reset.html'), 
    name="reset_password"),

    path('reset_passwd_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name = 'register/passwd_reset_sent.html'), 
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name = 'register/passwd_reset_confirm.html'), 
    name="password_reset_confirm"),

    path('reset_passwd_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name = 'register/passwd_reset_complete.html'), 
    name="password_reset_complete"),

] 