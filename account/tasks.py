from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_activation_code(email, code):
    import time
    time.sleep(10)
    send_mail(
        'Py25 shop',
        f'http://34.159.63.217/api/v1/account/activate/{code}',
        'bananad196@gmail.com',
        [email]
    )
