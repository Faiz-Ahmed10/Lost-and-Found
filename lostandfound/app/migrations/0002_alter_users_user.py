# Generated by Django 4.2.7 on 2023-11-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
