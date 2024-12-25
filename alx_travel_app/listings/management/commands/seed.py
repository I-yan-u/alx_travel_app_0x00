# Create a management command in listings/management/commands/seed.py to populate the database with sample listings data.
# The command should create 10 Listing objects with random data.

from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populate the database with sample listings data'

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(),
                description=fake.paragraph(),
                address=fake.street_address(),
                city=fake.city(),
                state=fake.state(),
                price=random.randint(100, 1000),
                bedrooms=random.randint(1, 5),
                bathrooms=random.uniform(1, 3),
                garage=random.choice([True, False]),
                sqft=random.randint(500, 5000),
                is_published=True
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample listings data'))

    