from django.contrib.auth.decorators import login_required
from django.urls import path, include

from baby_food.accounts.views import SignOutView, ProfileHomeView, SignUpView, SignInView, ProfileDetailsFormView, profile_update, ProfileDeleteView, ChangePasswordView

urlpatterns = (

    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('profile-welcome/', login_required(ProfileHomeView.as_view()), name='profile home'),
    path('profile/<int:pk>/', include([
        path('', login_required(ProfileDetailsFormView.as_view()), name='profile details'),
        path('edit/', login_required(profile_update), name='profile update'),
        path('delete/', login_required(ProfileDeleteView.as_view()), name='profile delete'),
        path('change/', login_required(ChangePasswordView.as_view()), name='change password'),
    ])),
)

