from datetime import datetime
from random import choice
from typing import List

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from faker import Faker
from faker.providers import BaseProvider

from accounts.models import FieldWork


class UserProvider(BaseProvider):

    """seed users"""

    def seeding_user(self) -> List:
        fake = Faker()
        users = get_user_model().objects.create(
            username=fake.first_name(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            password=fake.password(),
        )
        return users


class Command(BaseCommand):
    help = "creating field workd instances"

    def handle(self, *args, **kwargs):
        fake = Faker()

        fake.add_provider(UserProvider)

        for _ in range(10):
            FieldWork.objects.create(
                task_name=fake.paragraph(nb_sentences=1),
                location=fake.street_name(),
                activities=fake.paragraph(nb_sentences=5),
                assignee=fake.seeding_user(),
                date=fake.date_this_year(),
            )
