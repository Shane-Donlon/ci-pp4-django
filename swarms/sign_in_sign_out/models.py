from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class MyUser(AbstractUser):
    username = None
    email = models.EmailField(("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    verbose_name = "user"
    verbose_name_plural = "users"
    
    objects = CustomUserManager()
    def __str__(self):
        return self.email