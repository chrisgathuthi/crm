from celery import shared_task
from django.utils import timezone
import datetime
from django.core import serializers
from .models import Client

@shared_task(name="monthly invoice remainders")
def monthly_invoice_remainders():
    today_date = timezone.now()
    three_days_ago = today_date - timezone.timedelta(days=3)
    payment_due = Client.objects.filter(registration_date__range=[three_days_ago, today_date])
    mature_invoices = serializers.serialize("json",payment_due)
    return mature_invoices
    