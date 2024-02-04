# Generated by Django 4.2.6 on 2024-01-21 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0017_remove_staff_ticket_alter_fieldwork_assignee"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fieldwork",
            name="material",
        ),
        migrations.AddField(
            model_name="meterial",
            name="material",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="accounts.meterial",
            ),
        ),
    ]