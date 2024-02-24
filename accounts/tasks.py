import requests
import json
from celery import shared_task
from django.utils import timezone
import datetime
from .models import Client, ShortMessage
from .serializers import ClientPhoneNumberSerializer
from django.template.loader import render_to_string
from decouple import config
import pprint
from .utilities import clients_with_due_date


@shared_task(name="monthly invoice sms")
def send_invoice_sms(client=None):
    """send monthly due invoices via sms"""

    data = {
        "from": "TIARACONECT",
        "to": f"{client.phone_number.country_code}{client.phone_number.national_number}",
        "message": render_to_string(template_name="sms.txt",context={"client":client}),
        "refId": client.serial
    }
    try:
        response = requests.post(url="https://api.tiaraconnect.io/api/messaging/sendsms", data=json.dumps(data), headers={
            "Authorization": f"Bearer {config('SMSAPIKEY')}", 'Content-Type': 'application/json'})
    except Exception as e:
        print(e)
        # log this
        # top up when bal is low
        pass
    else:
        return 1

@shared_task(name="send scheduled messages")
def send_scheduled_sms(client=None, message=None):
    """send scheduled messages"""

    data = {
        "from": "TIARACONECT",
        "to": f"{client.phone_number.country_code}{client.phone_number.national_number}",
        "message": render_to_string(template_name="scheduled-sms.txt",context={"client":client, "message":message}),
        "refId": client.serial
    }
    try:
        response = requests.post(url="https://api.tiaraconnect.io/api/messaging/sendsms", data=json.dumps(data), headers={
            "Authorization": f"Bearer {config('SMSAPIKEY')}", 'Content-Type': 'application/json'})
    except Exception as e:
        print(e)
        # log this
        # top up when bal is low
        pass
    else:
        return 1

@shared_task(name="disseminate monthly billing invoices")
def execute_notification():

    queryset = clients_with_due_date()
    
    while len(queryset) >= 1: #refactor to use the batch processing
        for client in queryset:
            send_invoice_sms.delay(client=client)
        return 1


@shared_task(name="scheduled sms")
def send_scheduled_sms():

    """send scheduled messages"""

    clients = Client.objects.all()
    message = ShortMessage.objects.filter(is_sent=False)

    for client in clients:
        send_invoice_sms.delay(client=client, message=message)

    message.is_sent= True
    message.save()

    return 1