from django.core.mail import send_mail
from celery import shared_task
from spam.models import Contact

@shared_task
def send_spam():
    emails = [contact.email for contact in Contact.objects.all()]
    send_mail(
        'Py25 shop',
        f'Hello, visit our site',
        'bananad196@gmail.com',
        emails
    )
