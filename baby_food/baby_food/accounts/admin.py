from django.contrib import admin

from baby_food.accounts.forms import SignUpForm, UserEditForm
from baby_food.accounts.models import AppUser, Profile, Child
from django.contrib.auth import admin as auth_admin, get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    ordering = ('email',)
    list_display = ['username', 'email', 'date_joined', 'last_login']
    list_filter = ()
    form = SignUpForm
    add_form = UserEditForm
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'username',
                    'password1',
                    'password2',
                ),
            }),
        (
            'Personal info',
            {
                'fields': (
                    'email',
                    'number_of_children'
                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        # (
        #     'Important dates',
        #     {
        #         'fields': (
        #             'last_login',
        #             # 'date_joined',
        #         ),
        #     },
        # ),
    )

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         # 'fields': ('username',)
    #     }
    #      ),
    # )

    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    pass