# Generated by Django 2.0.2 on 2018-02-25 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoMark', '0008_auto_20180222_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramaccount',
            name='password',
            field=models.CharField(default='password', max_length=30),
            preserve_default=False,
        ),
    ]
