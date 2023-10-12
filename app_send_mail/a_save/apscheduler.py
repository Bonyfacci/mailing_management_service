from apscheduler.schedulers.background import BackgroundScheduler

from app_send_mail.service import send_email_to_clients

scheduler = BackgroundScheduler()


def start_scheduler():
    scheduler.add_job(func=send_email_to_clients, trigger="interval", seconds=30)
    scheduler.start()
