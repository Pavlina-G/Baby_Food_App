from dateutil.relativedelta import relativedelta

from django.contrib.auth.models import UserManager

from django.utils.translation import gettext_lazy as _
from django.core import validators
from baby_food.common.validators import validate_birth_date, validate_name
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth import models as auth_models

from baby_food.common.models import Location
from baby_food.menus.models import Menu


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin, ):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
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
        validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)],
    )

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['__all__']

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    first_name = models.CharField(
        max_length=30,
        blank=False,
        null=True,
        validators=[validate_name],
    )

    last_name = models.CharField(
        max_length=30,
        blank=False,
        null=True,
        validators=[validate_name],
    )

    profile_image = models.ImageField(
        upload_to='profile_pics',
        default='profile_pics/profile-icon.jpg'
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
    )

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.user.username


class Child(models.Model):
    first_name = models.CharField(
        max_length=30,
        blank=False,
        null=True,
        validators=[validate_name],
    )

    last_name = models.CharField(
        max_length=30,
        blank=False,
        null=True,
        validators=[validate_name],
    )

    date_of_birth = models.DateField(
        blank=False,
        null=True,
        validators=[validate_birth_date],
    )

    parent = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    @property
    def child_full_name(self):
        if self.first_name and self.last_name:
            return '{self.first_name} {self.last_name}'
        else:
            return 'No child data'

    class Meta:
        verbose_name_plural = 'Children'

    def __str__(self):
        return f'Child: {self.first_name} {self.last_name}'

    def last_menu_date(self):
        return self.date_of_birth + relativedelta(years=3)
