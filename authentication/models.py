from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    designation = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('email',)
