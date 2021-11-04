from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
from users.models import CustomUser


class UserSentence(models.Model):
    sentence_id = models.AutoField(
        primary_key=True,
        unique=True,
        db_column='sentence_id',
    )
    sentence_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        db_column="sentence_user"
    )
    sentence_text = models.TextField()


class UserWord(models.Model):
    word_id = models.AutoField(primary_key=True,  unique=True)
    user_id = models.ForeignKey(
        CustomUser,
        db_column='user_id',
        on_delete=models.CASCADE
    )
    sentence_id = models.ForeignKey(
        UserSentence,
        db_column='sentence_id',
        on_delete=models.CASCADE
    )
    word = models.TextField()
    strength = models.FloatField(default=1)
    trials = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('word_id', 'user_id',)
