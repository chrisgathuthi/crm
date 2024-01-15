# Generated by Django 4.2.6 on 2024-01-09 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0014_alter_fieldwork_isclosed"),
    ]

    operations = [
        migrations.CreateModel(
            name="Meterial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("quantity", models.PositiveIntegerField()),
                (
                    "provider",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="accounts.provider",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="fieldwork",
            name="material",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="accounts.meterial",
            ),
        ),
    ]