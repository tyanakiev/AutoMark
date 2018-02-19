from django.db import models


class InstagramAccount(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)


class InstagramSettings(models.Model):

    tags = models.CharField(max_length=1024)
    locations = models.CharField(max_length=1024)
    likes_hour = models.CharField(max_length=32)
    comments_hour = models.CharField(max_length=32)
    follows_hour = models.CharField(max_length=32)
    unfollows_hour = models.CharField(max_length=32)
    posted = models.CharField(max_length=32)
    comments = models.CharField(max_length=32)
