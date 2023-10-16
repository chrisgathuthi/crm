from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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
    service_plan = models.CharField(choices=SERVICE.choices, max_length=7)
    registration_date = models.DateTimeField(auto_created=True)


    def __str__(self):
        return self.first_name +""+ self.last_name
    

