from django.core.management.base import BaseCommand
from accounts.models import Client
from faker import Faker
from random import choice

from django.utils.timezone import now
from datetime import datetime


class Command(BaseCommand):

    help = "creating client instance"

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):
            Client.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                password=fake.password(),
                email=fake.free_email(),
                location=fake.last_name(),
                router=fake.ipv4(),
                phone_number=fake.msisdn(),
                service_plan=choice(["STATIC", "PPOE", "HOTSPOT"]),
                registration_date=datetime.now()
            )
        print("complete")
