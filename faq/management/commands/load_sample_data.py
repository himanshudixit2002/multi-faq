from django.core.management.base import BaseCommand
from faq.models import FAQ

SAMPLE_FAQS = [
    {
        'question': 'How do I reset my password?',
        'answer': '<p>Visit our <a href="/password-reset">password reset page</a> and follow these steps:<ol><li>Enter your email</li><li>Check your inbox</li><li>Click the reset link</li></ol></p>'
    },
    {
        'question': 'Where can I find documentation?',
        'answer': '<p>Explore our comprehensive guides at <a href="https://docs.example.com">docs.example.com</a> featuring:<ul><li>API references</li><li>SDK downloads</li><li>Code samples</li></ul></p>'
    }
]

class Command(BaseCommand):
    help = 'Loads attractive sample FAQ data'

    def handle(self, *args, **options):
        for faq in SAMPLE_FAQS:
            FAQ.objects.create(**faq)
        self.stdout.write(self.style.SUCCESS('Successfully loaded sample FAQs'))