# Generated by Django 4.2.6 on 2023-12-15 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Bandwidth",
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
                ("name", models.CharField(max_length=20)),
                ("size", models.PositiveIntegerField()),
                ("expiry", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Provider",
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
                ("serial_number", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=50)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("org_email", models.EmailField(max_length=254)),
                ("short_code", models.PositiveIntegerField()),
                ("join_date", models.DateTimeField(auto_now=True)),
                ("logo", models.ImageField(upload_to="")),
                ("is_activated", models.BooleanField(default=False)),
                (
                    "owner",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShortMessage",
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
                ("to", models.CharField(default="all", max_length=3)),
                (
                    "sender",
                    models.CharField(default="chris", editable=False, max_length=10),
                ),
                ("message", models.TextField()),
                ("schedule_time", models.DateTimeField(null=True)),
                ("timestamp", models.DateTimeField(auto_now=True)),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.provider",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MpesaTransaction",
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
                ("transaction_type", models.CharField(max_length=8)),
                ("transaction_id", models.CharField(max_length=10)),
                ("transaction_time", models.DateTimeField()),
                (
                    "transaction_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("short_code", models.PositiveIntegerField()),
                ("invoice_number", models.CharField(max_length=12)),
                ("bill_ref_number", models.CharField(max_length=10)),
                ("phone_number", models.CharField(max_length=12)),
                ("first_name", models.CharField(max_length=20)),
                ("middle_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.provider",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FieldWork",
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
                ("task_name", models.CharField(max_length=200)),
                ("location", models.CharField(max_length=200)),
                ("activities", models.TextField()),
                ("date", models.DateField()),
                ("isclosed", models.BooleanField(default=True)),
                (
                    "assignee",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="worker",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.provider",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Client",
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
                ("serial", models.CharField(blank=True, max_length=4, unique=True)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("password", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("location", models.CharField(max_length=20)),
                ("router", models.CharField(max_length=15)),
                (
                    "service_plan",
                    models.CharField(
                        choices=[
                            ("PPOE", "Ppoe"),
                            ("STATIC", "Static"),
                            ("HOTSPOT", "Hotspot"),
                        ],
                        max_length=7,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("ACTIVE", "Active"), ("INACTIVE", "Inactive")],
                        max_length=8,
                    ),
                ),
                ("registration_date", models.DateTimeField(auto_now=True, null=True)),
                (
                    "bandwidth",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="accounts.bandwidth",
                    ),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.provider",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bandwidth",
            name="provider",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="accounts.provider"
            ),
        ),
    ]
