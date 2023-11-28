# Generated by Django 4.2.7 on 2023-11-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_users_email_alter_users_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]