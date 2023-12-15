from .models import Client
from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(pre_save, sender=Client)
def set_serial_number(sender, instance, *args, **kwargs):
    last_count = Client.objects.count()
    instance.serial = f"HT-{last_count + 1}"
    instance_exist = Client.objects.order_by("id").last()
    # if instance_exist.serial == instance.serial:
    #     instance_exist.delete()

@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user= instance)