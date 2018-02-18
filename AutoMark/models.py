from django.db import models


class InstagramAccount(models.Model):
    username = models.CharField(max_length=30)
