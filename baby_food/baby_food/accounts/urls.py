from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView
from django.urls import path, include

from baby_food.accounts.views import profile_edit, SignOutView, ProfileHomeView, SignUpView, SignInView, \
    ProfileDetailsFormView, ProfileDeleteView, ChangePasswordView, child_update, ResetPasswordView, \
    ResetPasswordConfirmView

urlpatterns = (

    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('profile-welcome/', login_required(ProfileHomeView.as_view()), name='profile home'),
    path('child/edit/<int:user_id>-<int:pk>/', login_required(child_update), name='child update'),
    path('password/', include([
        path('reset/', ResetPasswordView.as_view(), name='reset password'),
        path('reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
             name='password_reset_done'),
        path('reset-confirm/<uidb64>/<token>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
        path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
             name='password_reset_complete'),
    ])),
    path('profile/', include([
        path('<int:pk>/', login_required(ProfileDetailsFormView.as_view()), name='profile details'),
        path('edit/<int:pk>/', login_required(profile_edit), name='profile edit'),
        path('delete/<int:pk>/', login_required(ProfileDeleteView.as_view()), name='profile delete'),
        path('change/<int:pk>/', login_required(ChangePasswordView.as_view()), name='change password'),
    ])),
)

from .signals import *
