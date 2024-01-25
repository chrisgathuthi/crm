import requests
import json
from celery import shared_task
from django.utils import timezone
import datetime
from .models import Client
from .serializers import ClientPhoneNumberSerializer
from django.template.loader import render_to_string

import pprint


@shared_task(name="monthly invoice remainders")
def monthly_invoice_remainders():
    """clients with due dates"""

    today_date = timezone.now() #every date 5
    three_days_ago = today_date - timezone.timedelta(days=3)
    payment_due = Client.objects.filter(registration_date__range=[three_days_ago, today_date]).only("phone_number")
    return payment_due




def send_invoice_sms(client=None):
    """send sms"""

    data = {
        "from": "TIARACONECT",
        "to": client.phone_number,
        "message": render_to_string(template_name="sms.txt",context={"client":client}),
        "refId": client.serial_no
    }
    try:
        response = requests.post(url="https://api.tiaraconnect.io/api/messaging/sendsms", data=json.dumps(data), headers={
            "Authorization": f"Bearer {config('SMSAPIKEY')}", 'Content-Type': 'application/json'})
    except Exception as e:
        # log this
        # top up when bal is low
        pass
    else:
        print(response.text)
        return 1

@shared_task(name="disseminate invoices")
def execute_notification(queryset=None):
    
    while len(queryset) >= 1: #refactor to use the batch processing
        for client in queryset:
            send_invoice_sms(client=client)
        return 1


