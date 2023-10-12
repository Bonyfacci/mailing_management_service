import logging
from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings

from app_send_mail.models import Newsletter, Logs
from app_send_mail.service import send_email_to_clients

logger = logging.getLogger(__name__)


def my_job():
    print('Работа my_job')
    to_send = False
    now = datetime.now()
    mailings = Newsletter.objects.filter(status='Запущена')

    for mailing in mailings:
        if mailing.time.strftime("%H:%M") == now.strftime("%H:%M"):
            last_attempt = Logs.objects.filter(message=mailing.id).last()

            if not last_attempt:
                to_send = True
            else:
                from_last = now.date() - last_attempt.attempt_status.date()
                if mailing.periodicity == Newsletter.MONTHLY and from_last == timedelta(
                        days=30) or mailing.periodicity == Newsletter.WEEKLY and from_last == timedelta(
                        days=7) or mailing.periodicity == Newsletter.DAILY and from_last == timedelta(days=1):
                    to_send = True

        if to_send:
            send_email_to_clients(mailing)
    print('Конец работы my_job')


def start_scheduler():
    print('Работа шедулера')
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_job(
        my_job,
        trigger=CronTrigger(second="*/10"),  # Every 10 seconds
        id="my_job",  # The `id` assigned to each job MUST be unique
        max_instances=1,
        replace_existing=True,
    )
    logger.info("Added job 'my_job'.")

    try:
        logger.info("Starting scheduler...")
        scheduler.start()
    except KeyboardInterrupt:
        logger.info("Stopping scheduler...")
        scheduler.shutdown()
        logger.info("Scheduler shut down successfully!")

    print('Конец работы шедулера')

