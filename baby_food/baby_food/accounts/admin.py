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
    form = UserEditForm
    add_form = SignUpForm

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'username',
                    # 'password1',
                    # 'password2',
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

    )

    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'parent')
    list_filter = ('parent',)
    list_select_related = ['parent']

    search_fields = ('parent_id__first_name', 'parent_id__last_name', 'first_name', 'last_name')
