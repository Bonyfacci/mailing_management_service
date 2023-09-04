from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from app_send_mail.models import Clients, Newsletter, Message, Logs


def home(request):
    return render(request, 'app_send_mail/home.html')


def get_start(request):
    return render(request, 'app_send_mail/course_work.html')


class ClientsListView(ListView):
    model = Clients


class ClientsCreateView(CreateView):
    model = Clients
    template_name = 'app_send_mail/form.html'
    fields = ('name', 'last_name', 'sur_name', 'email', 'comment')
    success_url = reverse_lazy('app_send_mail:clients')


class ClientsDetailView(DetailView):
    model = Clients
    template_name = 'app_send_mail/client_detail.html'
    fields = ('name', 'last_name', 'sur_name', 'email', 'comment')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        client = Clients.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Клиент - {client.name}'

        return context_data


class ClientsUpdateView(UpdateView):
    model = Clients
    template_name = 'app_send_mail/form.html'
    fields = ('name', 'last_name', 'sur_name', 'email', 'comment')
    success_url = reverse_lazy('app_send_mail:clients')


class ClientsDeleteView(DeleteView):
    model = Clients
    template_name = 'app_send_mail/delete_confirm.html'
    success_url = reverse_lazy('app_send_mail:clients')


class NewsletterListView(ListView):
    model = Newsletter


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    template_name = 'app_send_mail/form.html'
    fields = ('title', 'content')
    success_url = reverse_lazy('app_send_mail:message')


class LogsListView(ListView):
    model = Logs

