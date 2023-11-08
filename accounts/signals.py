from .models import Client
from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save, sender=Client)
def set_serial_number(sender, instance, *args, **kwargs):
    last_count = Client.objects.count()
    instance.serial = f"HT-{last_count + 1}"
    instance_exist = Client.objects.order_by("id").last()
    if instance_exist.serial == instance.serial:
        instance_exist.delete()