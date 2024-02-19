# Generated by Django 4.2.6 on 2024-02-19 11:47

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
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
                ("name", models.CharField(max_length=20, unique=True)),
                ("size", models.PositiveIntegerField()),
                ("timestamp", models.DateTimeField(auto_now=True)),
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
                ("serial", models.CharField(blank=True, max_length=7, unique=True)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, unique=True
                    ),
                ),
                ("password", models.CharField(max_length=50)),
                (
                    "email",
                    models.EmailField(
                        error_messages={
                            "unique": "This email has already been registered."
                        },
                        max_length=254,
                        unique=True,
                    ),
                ),
                ("location", models.CharField(max_length=20)),
                ("router", models.CharField(max_length=15)),
                (
                    "service_plan",
                    models.CharField(
                        choices=[
                            ("ppoe", "Ppoe"),
                            ("static", "Static"),
                            ("hotspot", "Hotspot"),
                        ],
                        max_length=7,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
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
                ("isclosed", models.BooleanField(default=False)),
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
                ("logo", models.ImageField(null=True, upload_to="logos")),
                ("is_activated", models.BooleanField(default=False)),
                (
                    "owner",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SmsGatewayResponse",
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
                ("sms_cost", models.CharField(max_length=5, null=True)),
                ("receiver", models.CharField(max_length=12)),
                ("message_id", models.CharField(max_length=40)),
                ("status", models.CharField(max_length=7)),
                ("status_code", models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "provider_information",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employee",
                        to="accounts.provider",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
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
                (
                    "schedule_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("is_sent", models.BooleanField(default=False)),
                ("timestamp", models.DateTimeField(auto_now=True)),
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
                ("bill_ref_number", models.CharField(max_length=10, null=True)),
                ("phone_number", models.CharField(max_length=12, null=True)),
                ("first_name", models.CharField(max_length=20, null=True)),
                ("middle_name", models.CharField(max_length=20, null=True)),
                ("last_name", models.CharField(max_length=20, null=True)),
                (
                    "client",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="payments",
                        to="accounts.client",
                    ),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="transactions",
                        to="accounts.provider",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Material",
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
                    "fieldwork",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="accounts.fieldwork",
                    ),
                ),
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
            name="assignee",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="worker",
                to="accounts.staff",
            ),
        ),
        migrations.AddField(
            model_name="fieldwork",
            name="provider",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="accounts.provider",
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="provider",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="accounts.provider",
            ),
        ),
        migrations.AddField(
            model_name="bandwidth",
            name="provider",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="accounts.provider",
            ),
        ),
    ]
