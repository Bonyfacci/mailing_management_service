import logging

from apscheduler.schedulers.background import BackgroundScheduler

from django.utils import timezone


from app_send_mail.a_save.service import send_email_to_clients
from app_send_mail.models import Newsletter, Logs
from app_send_mail.services import send_email_to_clients

logger = logging.getLogger(__name__)


def my_job():
    print(f'\n\nНачало my_job')
    now = timezone.now()

    newsletters = Newsletter.objects.filter(status=Newsletter.ACTIVE)
    print(f'Время {now} \nАктивных рассылок: {len(newsletters)}')

    for mailing_setting in newsletters:
        last_attempt = Logs.objects.filter(message=mailing_setting).order_by('send_time').first()
        print(last_attempt)

        if last_attempt:
            last_attempt_date = last_attempt.send_time
            time_difference = now - last_attempt_date

            if mailing_setting.periodicity == Newsletter.DAILY and time_difference.days >= 1:
                next_send_time = last_attempt_date + timezone.timedelta(days=1, hours=mailing_setting.time.hour,
                                                                        minutes=mailing_setting.time.minute)
                if now >= next_send_time:
                    send_email_to_clients(mailing_setting)
                    logger.info(f"Сообщение отправляется клиентам в новостной рассылке {mailing_setting.id}")

            elif mailing_setting.periodicity == Newsletter.WEEKLY and time_difference.days >= 7:
                next_send_time = last_attempt_date + timezone.timedelta(weeks=1, hours=mailing_setting.time.hour,
                                                                        minutes=mailing_setting.time.minute)
                if now >= next_send_time:
                    send_email_to_clients(mailing_setting)
                    logger.info(f"Сообщение отправляется клиентам в новостной рассылке {mailing_setting.id}")

            elif mailing_setting.periodicity == Newsletter.MONTHLY and time_difference.days >= 30:
                next_send_time = last_attempt_date + timezone.timedelta(days=30, hours=mailing_setting.time.hour,
                                                                        minutes=mailing_setting.time.minute)
                if now >= next_send_time:
                    send_email_to_clients(mailing_setting)
                    logger.info(f"Сообщение отправляется клиентам в новостной рассылке {mailing_setting.id}")

        else:
            send_time = timezone.datetime(now.year, now.month, now.day, mailing_setting.time.hour,
                                          mailing_setting.time.minute, tzinfo=timezone.get_current_timezone())
            if now >= send_time:
                send_email_to_clients(mailing_setting)
                logger.info(f"Сообщение отправляется клиентам в новостной рассылке {mailing_setting.id}")

    print(f'Конец my_job {now}')


scheduler = BackgroundScheduler()


def start_scheduler():
    scheduler.add_job(func=my_job, trigger="interval", id="my_job", seconds=30)
    scheduler.start()
