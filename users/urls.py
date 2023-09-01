# users/urls.py

from django.urls import path, re_path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',   views.register,                                                     name='register'),
    path('login/',      auth_views.LoginView.as_view(template_name='users/login.html'),     name='login'),
    path('logout/',     auth_views.LogoutView.as_view(template_name='users/logout.html'),   name='logout'),


    # _______ PASSWORD RESET __________#
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),

    re_path(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
            name='password_reset_confirm'),
    # _______ PASSWORD RESET END __________#

]
