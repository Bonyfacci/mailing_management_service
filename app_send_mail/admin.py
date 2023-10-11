from django.contrib import admin

from app_send_mail.models import Client, Newsletter, Message, Logs


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'last_name', 'sur_name', 'email', 'comment', 'owner',)
    search_fields = ('email', 'name', 'last_name', 'comment')
    list_filter = ('owner',)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time', 'periodicity', 'status', 'message', 'owner')
    list_filter = ('periodicity', 'status', 'owner')
    search_fields = ('message',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'owner')
    search_fields = ('title', 'content')


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'send_time', 'attempt_status', 'server_response')
    list_filter = ('attempt_status', 'server_response')
    search_fields = ('owner',)
