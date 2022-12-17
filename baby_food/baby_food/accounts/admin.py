from django.contrib import admin

from baby_food.accounts.forms import SignUpForm
from baby_food.accounts.models import AppUser
from django.contrib.auth import admin as auth_admin, get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    ordering = ('email',)
    list_display = ['email', 'date_joined', 'last_login']
    list_filter = ()
    add_form = SignUpForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
