# Generated by Django 2.0.2 on 2018-02-25 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AutoMark', '0009_instagramaccount_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instagramaccount',
            name='password',
        ),
    ]
