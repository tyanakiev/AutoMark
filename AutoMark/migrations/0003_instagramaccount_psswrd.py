# Generated by Django 2.0.2 on 2018-02-18 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoMark', '0002_instagramaccounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramaccount',
            name='psswrd',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
