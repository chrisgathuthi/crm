from celery import shared_task
from django.utils import timezone
import datetime
from .models import Client
from .serializers import ClientPhoneNumberSerializer

import pprint
@shared_task(name="monthly invoice remainders")
def monthly_invoice_remainders():

    """clients with due dates"""

    today_date = timezone.now()
    three_days_ago = today_date - timezone.timedelta(days=3)
    payment_due = Client.objects.filter(registration_date__range=[three_days_ago, today_date]).only("phone_number")
    return payment_due

@shared_task(name="disseminate invoices")
def send_invoice_sms(queryset=None):
    pass
    