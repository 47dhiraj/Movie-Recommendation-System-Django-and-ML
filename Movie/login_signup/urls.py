from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [

    path('login/', views.loginPage, name="login"),
    path('register/', views.clientregisterPage, name="clientregister"),
    path('adminregister/', views.adminregisterPage, name="adminregister"),



    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="login_signup/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="login_signup/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="login_signup/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="login_signup/password_reset_done.html"),
         name="password_reset_complete"),



    path('logoutall/', views.logoutall, name="logoutall"),

    path('accounts/', include('allauth.urls')),    

    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),

]
