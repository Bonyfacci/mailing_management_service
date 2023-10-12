from datetime import datetime, timedelta
import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.core.management.base import BaseCommand

from django_apscheduler import util
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from app_send_mail.models import Newsletter, Logs
from app_send_mail.services import send_message

logger = logging.getLogger(__name__)


def my_job():
    print('Начало my_job')
    to_send = False
    now = datetime.now()
    mailings = Newsletter.objects.filter(status=Newsletter.ACTIVE)

    for mailing in mailings:
        if mailing.time.strftime("%H:%M") == now.strftime("%H:%M"):
            last_attempt = Logs.objects.filter(message=mailing.id).last()

            if not last_attempt:
                to_send = True
            else:
                from_last = now.date() - last_attempt.send_time.date()
                if mailing.periodicity == Newsletter.MONTHLY and from_last == timedelta(
                        days=30) or mailing.periodicity == Newsletter.WEEKLY and from_last == timedelta(
                        days=7) or mailing.periodicity == Newsletter.DAILY and from_last == timedelta(days=1):
                    to_send = True

        if to_send:
            send_message(mailing)

    print(f'Конец my_job {now}')


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),  # Every 10 seconds
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
