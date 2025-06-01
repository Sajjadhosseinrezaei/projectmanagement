from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=150, unique=True)


    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.name
