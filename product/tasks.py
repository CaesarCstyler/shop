from django.core.mail import send_mail
from celery import shared_task
from spam.models import Contact


@shared_task
def big_function():
    import time
    time.sleep(10)

@shared_task
def send_product_news(title, price):
    emails = [contact.email for contact in Contact.objects.all()]
    send_mail(
        'Py25 shop',
        f'Hello, we have new product on our site! {title} with price {price}',
        'bananad196@gmail.com',
        emails
    )
