from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime


class CustomUser(AbstractUser):
    pass

    def __int__(self):
        return self.id

    def __str__(self):
        return str(self.username)


class UserMeta(models.Model):
    user_id = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
        unique=True,
    )
    test_field = models.TextField(blank=True, default="test field")

    def __str__(self):
        return str(self.user_id)
