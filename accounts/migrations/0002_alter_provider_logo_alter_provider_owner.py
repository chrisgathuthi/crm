# Generated by Django 4.2.6 on 2023-12-20 08:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import accounts.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="provider",
            name="logo",
            field=models.ImageField(
                null=True, upload_to=accounts.models.Provider.log_directory
            ),
        ),
        migrations.AlterField(
            model_name="provider",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
