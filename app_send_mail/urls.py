from django.urls import path

from app_send_mail.apps import AppSendMailConfig

from app_send_mail.views import home, get_start
from app_send_mail.views import ClientsListView, ClientsCreateView, ClientsDetailView, ClientsUpdateView, \
    ClientsDeleteView
from app_send_mail.views import MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView
from app_send_mail.views import NewsletterListView, NewsletterCreateView, NewsletterUpdateView, NewsletterDeleteView
from app_send_mail.views import LogsListView

app_name = AppSendMailConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('course_work/', get_start, name='get_start'),

    # ---------------------------------------------------------------- Клиенты --------------------------------
    path('clients/', ClientsListView.as_view(), name='clients'),
    path('clients/add/', ClientsCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/', ClientsDetailView.as_view(), name='client_detail'),
    path('clients/edit/<int:pk>/', ClientsUpdateView.as_view(), name='client_edit'),
    path('clients/delete/<int:pk>/', ClientsDeleteView.as_view(), name='client_delete'),

    # ---------------------------------------------------------------- Новостная рассылка ------------------------------
    path('newsletter/', NewsletterListView.as_view(), name='newsletter'),
    path('newsletter/add/', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletter/edit/<int:pk>/', NewsletterUpdateView.as_view(), name='newsletter_edit'),
    path('newsletter/delete/<int:pk>/', NewsletterDeleteView.as_view(), name='newsletter_delete'),

    # ---------------------------------------------------------------- Сообщения --------------------------------
    path('message/', MessageListView.as_view(), name='message'),
    path('message/add/', MessageCreateView.as_view(), name='message_create'),
    path('message/edit/<int:pk>/', MessageUpdateView.as_view(), name='message_edit'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

    # ---------------------------------------------------------------- Логи --------------------------------
    path('logs/', LogsListView.as_view(), name='logs'),
]
