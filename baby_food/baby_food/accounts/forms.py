from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model, authenticate
from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

from baby_food.accounts.models import Profile, AppUser, Child

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'number_of_children')
        field_classes = {
            'username': auth_forms.UsernameField,
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username: ',
                },
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email: ',
                },
            ),
        }

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            user=user,
        )
        children_numbers = user.number_of_children

        if commit:
            profile.save()
            for _ in range(children_numbers):
                child = Child(parent=profile)
                child.save()

        return user


class SignInForm(auth_forms.AuthenticationForm):
    pass


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        exclude = ('date_joined',)
        # fields = '__all__'
        field_classes = {'username': auth_forms.UsernameField}


class BaseUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email',)
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
                'class': 'form-control',

            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
            })
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
        }


class UserForm(BaseUserForm):
    pass


class UserUpdateForm(BaseUserForm):
    pass


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ('user',)
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
            }),

        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_image': 'Profile Image',
            'location': 'Location',
        }


class ProfileForm(BaseProfileForm):
    pass


class ProfileEditForm(BaseProfileForm):
    pass


class BaseChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ('first_name', 'last_name', 'date_of_birth')

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Child First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Child Last Name',
            }),
            'date_of_birth': forms.DateInput(attrs={
                'placeholder': 'Child Birth Date',
            }),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Birth Date',
        }


class ChildForm(BaseChildForm):
    pass


class ChildEditForm(BaseChildForm):
    pass
