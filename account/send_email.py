from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Py25 shop',
        f'http://localhost:8000/account/activate/{code}',
        'bananad196@gmail.com',
        [email]
    )

def send_reset_password_code(email, code):
    send_mail(
        'Py25 shop',
        f'Reset activataion code: {code}',
        'bananad196@gmail.com',
        [email]
    )
