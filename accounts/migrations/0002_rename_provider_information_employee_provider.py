# Generated by Django 4.2.6 on 2024-07-02 13:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employee",
            old_name="provider_information",
            new_name="provider",
        ),
    ]
