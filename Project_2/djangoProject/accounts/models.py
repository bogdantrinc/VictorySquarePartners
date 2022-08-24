from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import UserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    address =models.CharField(max_length=100, default='', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
