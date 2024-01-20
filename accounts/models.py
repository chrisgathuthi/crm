import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Provider(models.Model):  # company name
    """provider model, each company profile"""

    def log_directory(instance, filename):
        return f"logos_{instance.id}/{filename}"

    serial_number = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)  # co, name
    location = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    org_email = models.EmailField()
    short_code = models.PositiveIntegerField()  # activate short code
    join_date = models.DateTimeField(auto_now=True)
    owner = models.OneToOneField(get_user_model(), on_delete=models.SET_NULL, null=True)
    logo = models.ImageField(upload_to="logos", null=True)  # set default
    is_activated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.location}"


class Bandwidth(models.Model):
    """internet bandwidth"""

    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20, unique=True)
    size = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.size) + "mbs"


class Client(models.Model):

    """client table model"""

    class SERVICE(models.TextChoices):
        PPOE = "PPOE"
        STATIC = "STATIC"
        HOTSPOT = "HOTSPOT"

    class STATUS(models.TextChoices):  # user status
        active = "ACTIVE"
        inactive = "INACTIVE"

    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    serial = models.CharField(unique=True, max_length=7, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=20)
    router = models.CharField(max_length=15)
    bandwidth = models.ForeignKey(to=Bandwidth, on_delete=models.SET_NULL, null=True)
    service_plan = models.CharField(choices=SERVICE.choices, max_length=7)
    status = models.CharField(max_length=8, choices=STATUS.choices)
    registration_date = models.DateTimeField(
        auto_now=True, blank=True, null=True
    )  # change this

    def __str__(self):
        return self.first_name + "" + self.last_name
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Meterial(models.Model):
    """field work materils"""

    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class FieldWork(models.Model):
    """field work activities"""

    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    material = models.ForeignKey(Meterial, on_delete=models.SET_NULL, null=True)
    task_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    activities = models.TextField()
    assignee = models.ForeignKey(
        to="Staff", on_delete=models.SET_NULL, null=True, related_name="worker"
    )
    date = models.DateField()
    isclosed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name + "by" + self.assignee


class ShortMessage(models.Model):
    """sms sent to clients"""

    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    to = models.CharField(max_length=3, default="all")  # to client instance
    sender = models.CharField(max_length=10, default="chris", editable=False)  # tenant
    message = models.TextField()
    schedule_time = models.DateTimeField(default=timezone.now)
    is_sent = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"sent to {self.to } at {self.timestamp}"


class MpesaTransaction(models.Model):
    """mpesa transactions"""

    provider = models.ForeignKey(
        Provider, on_delete=models.SET_NULL, null=True, related_name="transactions"
    )
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, null=True, related_name="payments"
    )
    transaction_type = models.CharField(max_length=8)
    transaction_id = models.CharField(max_length=10)
    transaction_time = models.DateTimeField()
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    short_code = models.PositiveIntegerField()
    invoice_number = models.CharField(max_length=12)
    bill_ref_number = models.CharField(max_length=10, null=True)  # paybill only
    phone_number = models.CharField(max_length=12, null=True)
    first_name = models.CharField(max_length=20, null=True)
    middle_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name}"

    @property
    def full_name(self):
        """full client name"""
        return f"{self.first_name} {self.last_name}"

class Staff(models.Model):

    """staff users model"""
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="employee")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name