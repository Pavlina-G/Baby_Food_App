from django.contrib.auth.decorators import login_required
from django.urls import path, include

from baby_food.accounts.views import SignOutView, ProfileHomeView, SignUpView, SignInView, ProfileDetailsFormView, profile_update, ProfileDeleteView

urlpatterns = (
    # path('sign-up/', sign_up , name='sign up'),
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    # path('sign-in/', sign_in_view, name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('profile-welcome/', login_required(ProfileHomeView.as_view()), name='profile home'),
    path('profile/<int:pk>/', include([
        # path('', ProfileDetailsView.as_view(), name='profile details'),
        path('', login_required(ProfileDetailsFormView.as_view()), name='profile details'),
        # path('edit/', login_required(ProfileEditFormView.as_view()), name='profile edit'),
        path('edit/', login_required(profile_update), name='profile update'),
        path('delete/', ProfileDeleteView.as_view(), name='profile delete'),
    ])),
)

