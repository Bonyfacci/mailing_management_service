from django.apps import AppConfig


class AppSendMailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_send_mail'
    verbose_name = 'Отправка почты'

    # def ready(self):
    #     from app_send_mail.apscheduler import start_scheduler
    #     start_scheduler()

    def ready(self):
        from app_send_mail.runapscheduler import start_scheduler
        start_scheduler()
