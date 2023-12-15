from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import uuid

class Provider(models.Model):#company name
    """provider model, each company profile"""
     
    def log_directory(instance, filename):
        return f"logos_{instance.id}/{filename}"
    
    serial_number = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)#co, name
    location = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    org_email = models.EmailField()
    short_code = models.PositiveIntegerField()#activate short code
    join_date = models.DateTimeField(auto_now=True)
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=log_directory, null=True)#set default
    is_activated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.location}"


class Bandwidth(models.Model):
    """internet bandwidth"""
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    size = models.PositiveIntegerField()
    expiry = models.DateField()

    def __str__(self):
        return str(self.size) +"mbs"


class Client(models.Model):

    """client table model"""

    class SERVICE(models.TextChoices):
        PPOE = "PPOE"
        STATIC = "STATIC"
        HOTSPOT = "HOTSPOT"

    class STATUS(models.TextChoices):  # user status
        active = "ACTIVE"
        inactive = "INACTIVE"

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    serial = models.CharField(unique=True, max_length=4, blank=True)
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


class FieldWork(models.Model):
    """field work activities"""
    
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    activities = models.TextField()
    assignee = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, null=True, related_name="worker"
    )
    date = models.DateField()
    isclosed = models.BooleanField(default=True)

    def __str__(self):
        return self.task_name + "by" + self.assignee

class ShortMessage(models.Model):
    """sms sent to clients"""
    
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    to = models.CharField(max_length=3, default="all")#to client instance
    sender = models.CharField(max_length=10, default='chris', editable=False)#tenant
    message = models.TextField()
    schedule_time = models.DateTimeField(null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"sent to {self.to } at {self.timestamp}"

class MpesaTransaction(models.Model):
    """mpesa transactions """
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=8)
    transaction_id = models.CharField(max_length=10)
    transaction_time = models.DateTimeField()
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    short_code = models.PositiveIntegerField()
    invoice_number = models.CharField(max_length=12)#msdsin
    bill_ref_number = models.CharField(max_length=10)#paybill only
    phone_number = models.CharField(max_length=12)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.first_name} {self.msdin}"
