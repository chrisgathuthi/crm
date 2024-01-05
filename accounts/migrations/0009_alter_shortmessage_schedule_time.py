# Generated by Django 4.2.6 on 2023-12-26 14:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0008_alter_shortmessage_schedule_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shortmessage",
            name="schedule_time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
