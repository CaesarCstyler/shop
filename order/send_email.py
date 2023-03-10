from django.core.mail import send_mail

def send_order_confirmation_code(email, code, name, price):
    full_link = f'Hi, confirm your order of {name} total price: {price}\n\n http://34.159.63.217/api/v1/order/confirm/{code}'

    send_mail(
        'Order from shop',
        full_link,
        'bananad196@gmail.com',
        [email]
    )
