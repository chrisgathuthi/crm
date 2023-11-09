from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Client(models.Model):

    """client table model"""

    class SERVICE(models.TextChoices):
        PPOE = "PPOE"
        STATIC = "STATIC"
        HOTSPOT = "HOTSPOT"

    serial = models.CharField(unique=True, max_length=4, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=20)
    router = models.CharField(max_length=15)
    # bandwidth = models.IntegerField()
    service_plan = models.CharField(choices=SERVICE.choices, max_length=7)
    # status = models.CharField(max_length=10)
    registration_date = models.DateTimeField(auto_now=True,blank=True, null=True)#change this


    def __str__(self):
        return self.first_name +""+ self.last_name
    

class FieldWork(models.Model):
    """field work activities"""

    task_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    activities = models.TextField()
    assignee = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="worker")
    date = models.DateField()

    def __str__(self):
        return self.task_name + "by" + self.assignee