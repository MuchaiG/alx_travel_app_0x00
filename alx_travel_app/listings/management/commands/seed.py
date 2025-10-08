from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_listings = [
            {
                "title": "Cozy Apartment in Nairobi",
                "description": "A comfortable apartment in the heart of Nairobi.",
                "price": 50.0,
                "location": "Nairobi",
            },
            {
                "title": "Beach House in Mombasa",
                "description": "Enjoy the ocean view from this beautiful beach house.",
                "price": 120.0,
                "location": "Mombasa",
            },
            {
                "title": "Mountain Cabin in Nyeri",
                "description": "A peaceful retreat in the mountains.",
                "price": 80.0,
                "location": "Nyeri",
            },
        ]

        for data in sample_listings:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS('Sample listings seeded successfully.'))