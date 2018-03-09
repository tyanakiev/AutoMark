from django.db import models
from django.contrib.auth.hashers import make_password


class InstagramAccount(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)


class InstagramSettings(models.Model):

    id = models.AutoField(primary_key=True)
    tags = models.CharField(max_length=1024)
    locations = models.CharField(max_length=1024)
    likes_hour = models.CharField(max_length=32)
    comments_hour = models.CharField(max_length=32)
    follows_hour = models.CharField(max_length=32)
    unfollows_hour = models.CharField(max_length=32)
    comments = models.CharField(max_length=32)


class InstagramCeleryTask(models.Model):
    account_id = models.AutoField(primary_key=True)
    task_id = models.CharField(max_length=30)
    status = models.CharField(max_length=32)

