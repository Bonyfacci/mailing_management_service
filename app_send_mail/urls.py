from django.urls import path

from app_send_mail.apps import AppSendMailConfig
from app_send_mail.views import home, get_start, ClientsListView, NewsletterListView, MessageListView, LogsListView, \
    ClientsCreateView, MessageCreateView, ClientsDeleteView, ClientsUpdateView, ClientsDetailView

app_name = AppSendMailConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('course_work/', get_start, name='get_start'),

    path('clients/', ClientsListView.as_view(), name='clients'),
    path('clients/add/', ClientsCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/', ClientsDetailView.as_view(), name='client_detail'),
    path('clients/edit/<int:pk>/', ClientsUpdateView.as_view(), name='client_edit'),
    path('clients/delete/<int:pk>/', ClientsDeleteView.as_view(), name='client_delete'),

    path('newsletter/', NewsletterListView.as_view(), name='newsletter'),
    path('message/', MessageListView.as_view(), name='message'),
    path('message/add/', MessageCreateView.as_view(), name='message_create'),
    path('logs/', LogsListView.as_view(), name='logs'),
]
