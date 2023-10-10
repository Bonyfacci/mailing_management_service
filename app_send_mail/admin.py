from django.contrib import admin

from app_send_mail.models import Client, Newsletter, Message, Logs


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'last_name', 'sur_name', 'email', 'comment')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time', 'periodicity')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content')


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'send_time', 'attempt_status', 'server_response')
