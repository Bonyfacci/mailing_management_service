from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string


def send_verification_email(email, user_code):
    subject = 'Поздравляем с регистрацией'
    message = f'Вы зарегистрировались на нашей платформе!' \
              f'\n\nВаш код верификации: {user_code}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)


def send_password(email, new_password):
    subject = 'Вы сменили пароль'
    message = f'Ваш новый пароль: {new_password}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

