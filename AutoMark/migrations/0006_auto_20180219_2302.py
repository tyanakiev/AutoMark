# Generated by Django 2.0.2 on 2018-02-19 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoMark', '0005_remove_instagramaccount_psswrd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramaccount',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
