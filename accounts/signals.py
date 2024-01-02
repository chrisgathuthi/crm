from .models import Client
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from random import randint
from rest_framework.authtoken.models import Token

@receiver(pre_save, sender=Client)
def set_serial_number(sender, instance, *args, **kwargs):
    if instance.serial ==  "":
        instance.serial = f"HT{randint(999,9999)}"
        instance.password = instance.serial


@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user= instance)