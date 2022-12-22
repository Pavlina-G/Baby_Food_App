from django.contrib.auth.decorators import login_required
from django.urls import path, include

from baby_food.accounts.views import profile_edit, SignOutView, ProfileHomeView, SignUpView, SignInView, \
    ProfileDetailsFormView, ProfileDeleteView, ChangePasswordView, child_update

urlpatterns = (

    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('profile-welcome/', login_required(ProfileHomeView.as_view()), name='profile home'),
    path('child/edit/<int:user_id>-<int:pk>/', login_required(child_update), name='child update'),
    path('profile/', include([
        path('<int:pk>/', login_required(ProfileDetailsFormView.as_view()), name='profile details'),
        path('edit/<int:pk>/', login_required(profile_edit), name='profile edit'),
        path('delete/<int:pk>/', login_required(ProfileDeleteView.as_view()), name='profile delete'),
        path('change/<int:pk>/', login_required(ChangePasswordView.as_view()), name='change password'),
    ])),
)

