import logging
from smtplib import SMTPException

from django.core.mail import send_mail
from django.conf import settings
from app_send_mail.models import Client, Newsletter, Message, Logs
from datetime import datetime
import pytz

logger = logging.getLogger(__name__)


def send_email_to_clients(mailing_settings):
    print('Работа отправки')

    clients = mailing_settings.clients.all()
    clients_list = [client.email for client in clients]

    server_response = 'None'
    status = Logs.STATUS_ERROR

    try:
        letter = send_mail(
            subject=mailing_settings.message.title,
            message=mailing_settings.message.content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=clients_list,
        )

        if letter:
            status = Logs.STATUS_OK
            server_response = 'Успешно'

    except SMTPException as e:
        server_response = str(e)
        logger.error(f'Исключение SMTPException: {e}')
    else:
        logger.info('Успешно')

    if server_response:
        logger.info(f'Ответ сервера: {server_response}')

    Logs.objects.create(
        message=mailing_settings,
        attempt_status=status,
        server_response=server_response
    )

    print('Конец работы отправки')
