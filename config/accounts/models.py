from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
