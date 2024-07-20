# Generated by Django 4.2.6 on 2024-07-19 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0005_remove_material_name_material_inventory_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="material",
            name="fieldwork",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="accounts.fieldwork",
            ),
        ),
    ]
