# Generated by Django 2.0.2 on 2018-02-22 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoMark', '0007_instagramsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramsettings',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
