import uuid

import pytz
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from project.commons.models import TimeStampModel, File
from .manager import UserManager


class User(TimeStampModel, AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.UUIDField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
        default=uuid.uuid4
    )
    email = models.EmailField(max_length=45, unique=True, error_messages={
        'unique': "A user with that email already exists.",
    }, )
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45, null=True, blank=True)
    last_name = models.CharField(max_length=45)
    profile_picture = models.ForeignKey(File, on_delete=models.CASCADE, null=True, blank=True)
    time_zone = models.CharField(default='Asia/Kathmandu',
                                 choices=[(tz, tz) for tz in pytz.all_timezones],
                                 max_length=70)

    # last login seems important because, last_activity can only be obtained from AuthToken class
    # if the user deletes all his session , then even this last_activity information is lost
    last_login = models.DateTimeField('last login', blank=True, null=True)
    last_activity = models.DateTimeField('last activity', blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)

    contact_number = models.CharField(max_length=14, null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    ACCOUNT_REGISTRATION_FIELDS = ['email', 'first_name', 'last_name', 'password', 'contact_number']

    @property
    def profile_picture_thumb(self):
        if self.profile_picture:
            return self.profile_picture.file.url

        from django.templatetags.static import static
        return static('user/images/default-pp.jpeg')

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def display_name(self):
        return f"{self.first_name} {self.last_name}" if not self.middle_name \
            else f"{self.first_name} {self.middle_name} {self.last_name}"

    def __str__(self):
        return f"{self.email}"
