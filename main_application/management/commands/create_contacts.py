from django.core.management import BaseCommand
from django.urls import reverse
from faker import Faker

from main_application.models import Contact


class Command(BaseCommand):
    help = 'Creates 100 unique contact forms'

    def handle(self, *args, **options):
        fake = Faker()
        num_forms = 100

        for _ in range(num_forms):
            name = fake.name()
            email = fake.email()
            subject = fake.sentence(nb_words=5)
            message = fake.paragraph(nb_sentences=3)
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created {num_forms} contact forms.'))
