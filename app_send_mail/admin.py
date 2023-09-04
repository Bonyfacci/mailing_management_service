from django.contrib import admin

from app_send_mail.models import Clients, Newsletter, Message, Logs


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'last_name', 'sur_name', 'email', 'comment')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time', 'periodicity', 'is_active')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content')


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time', 'attempt_status', 'answer')
