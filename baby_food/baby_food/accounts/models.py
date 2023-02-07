import datetime
from datetime import timedelta

from django.contrib.auth.models import UserManager
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth import models as auth_models
from baby_food.accounts.managers import AppUserManager
from baby_food.menu_app.models import Menu


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin, ):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        # help_text=_(
        #     "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        # ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        validators={
            validators.EmailValidator,
        }
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
    )

    number_of_children = models.PositiveIntegerField(
        default=1,
    )

    # User credentials consist of `email` and `password`
    # USERNAME_FIELD = 'email'

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "number_of_children"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_user_email(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    # objects = AppUserManager()

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    first_name = models.CharField(
        max_length=30
    )

    last_name = models.CharField(
        max_length=30
    )

    profile_image = models.ImageField(
        upload_to='profile_pics',
        default='profile_pics/profile-icon.jpg'
    )

    # orders = models.ManyToManyField(Menu, blank=True)

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.user.username


class Child(models.Model):
    first_name = models.CharField(
        max_length=30
    )

    last_name = models.CharField(
        max_length=30
    )

    date_of_birth = models.DateField(
        default=timezone.now
    )
    parent = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'Children'

    def __str__(self):
        return f'Child: {self.first_name} {self.last_name}'
        # return f'Email: {self.parent.user.username} Child: {self.first_name} {self.last_name}'



    # last_voucher_on = date_of_birth + timedelta(days=365*3)
