# Generated by Django 4.2.6 on 2023-12-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_provider_logo_alter_provider_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="provider",
            name="logo",
            field=models.ImageField(null=True, upload_to="logos"),
        ),
    ]
