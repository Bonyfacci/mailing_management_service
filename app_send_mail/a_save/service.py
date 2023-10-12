from django.core.mail import send_mail
from django.conf import settings
from app_send_mail.models import Client, Newsletter, Message, Logs
from datetime import datetime
import pytz


def send_email_to_clients():
    print(f"Отправка рассылки {datetime.now()}")

    now = datetime.now(pytz.utc)

    newletters = Newsletter.objects.filter(status='Запущена').filter(time__lte=now)

    for newletter in newletters:
        clients = list(newletter.client_id.values())
        for client in clients:
            try:
                send_mail(
                    subject=newletter.message.title,
                    message=newletter.message.content,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client['email'], ]
                )

                log = Logs(
                    message=newletter,
                    client=Client.objects.get(id=client['id']),
                    send_time=now,
                    attempt_status='success',
                )

                log.save()

                print(f'Отправлено {client["email"]}')

            except Exception as e:
                print(f'Ошибка {e}')
