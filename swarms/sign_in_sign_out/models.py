from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=50, verbose_name="First Name", null=True, blank=False)
    last_name = models.CharField(
        max_length=150, verbose_name="Last Name", null=True, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=False)
    county = models.CharField(max_length=50, null=True, blank=False)

    def __str(self):
        return f"{self.first_name} {self.last_name}"
