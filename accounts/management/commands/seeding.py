from django.core.management.base import BaseCommand
from accounts.models import Client, Bandwidth
from faker import Faker
from random import choice
from faker.providers import BaseProvider
from django.utils.timezone import now
from datetime import datetime


class BandwidthProvider(BaseProvider):

    def seed_bandwidth(self):
        faker = Faker()
        results = Bandwidth.objects.create(name=faker.first_name(),size=faker.random_digit(), expiry=faker.date())
        return results
        
class Command(BaseCommand):
    help = "creating client instance"

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(BandwidthProvider)

        for _ in range(10):
            Client.objects.create(
                serial="",
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                password=fake.password(),
                email=fake.free_email(),
                location=fake.last_name(),
                router=fake.ipv4(),
                phone_number=fake.msisdn(),
                bandwidth=fake.seed_bandwidth(),
                service_plan=choice(["STATIC", "PPOE", "HOTSPOT"]),
                status=choice(["ACTIVE", "INACTIVE"]),
                registration_date=datetime.now(),
            )
        print("complete")
