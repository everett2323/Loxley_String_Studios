from django.test import TestCase
from django.urls import reverse
from main_application.models import Contact
from faker import Faker

class ContactFormTest(TestCase):
    def test_create_contact_forms(self):
        fake = Faker()
        num_forms = 100

        for _ in range(num_forms):
            name = fake.name()
            email = fake.email()
            subject = fake.sentence(nb_words=5)
            message = fake.paragraph(nb_sentences=3)

            response = self.client.post(reverse('contact'), {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            })
            self.assertEqual(response.status_code, 302)  # Check for redirect status code

        self.assertEqual(Contact.objects.count(), num_forms)