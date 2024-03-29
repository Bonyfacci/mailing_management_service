import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from app_blog.models import Blog
from app_send_mail.forms import ClientsCreateForm, MessageCreateForm, NewsletterCreateForm
from app_send_mail.models import Client, Newsletter, Message, Logs


def home(request):
    return render(request, 'app_send_mail/home.html')


def get_start(request):
    blog_list = Blog.objects.all()

    random_blog = random.sample(list(blog_list), 3)
    context = {
        'blog_list': random_blog,
        'settings_list': Newsletter.objects.all(),
        'active_settings': Newsletter.objects.filter(status='Запущена'),
        'client_list': Client.objects.all(),
    }
    return render(request, 'app_send_mail/course_work.html', context)


# ---------------------------------------------------------------- Клиенты --------------------------------

class ClientsListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'app_send_mail/clients_list.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            owner=self.request.user
        )
        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)

        return queryset


class ClientsCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientsCreateForm
    template_name = 'app_send_mail/client_form.html'
    success_url = reverse_lazy('app_send_mail:clients')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClientsDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'app_send_mail/client_detail.html'
    fields = ('name', 'last_name', 'sur_name', 'email', 'comment')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        client = Client.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Клиент - {client.name}'

        return context_data


class ClientsUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientsCreateForm
    template_name = 'app_send_mail/client_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('app_send_mail:clients')


class ClientsDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'app_send_mail/client_delete_confirm.html'
    success_url = reverse_lazy('app_send_mail:clients')


# ---------------------------------------------------------------- Новостная рассылка --------------------------------

class NewsletterListView(LoginRequiredMixin, ListView):
    model = Newsletter
    template_name = 'newsletter_list.html'

    def get_queryset(self):
        queryset = Newsletter.objects.all()

        if not self.request.user.is_staff:
            queryset = queryset.filter(
                owner=self.request.user
            )

        return queryset


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterCreateForm
    template_name = 'app_send_mail/newsletter_form.html'
    success_url = reverse_lazy('app_send_mail:newsletter')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields['message'].queryset = Message.objects.filter(owner=self.request.user)
        form.fields['client_id'].queryset = Client.objects.filter(owner=self.request.user)

        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterCreateForm
    success_url = reverse_lazy('app_send_mail:newsletter')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields['message'].queryset = Message.objects.filter(owner=self.request.user)
        form.fields['client_id'].queryset = Client.objects.filter(owner=self.request.user)

        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('app_send_mail:newsletter')


# ---------------------------------------------------------------- Сообщения --------------------------------

class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'app_send_mail/message_list.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            owner=self.request.user
        )
        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)

        return queryset


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageCreateForm
    template_name = 'app_send_mail/message_form.html'
    success_url = reverse_lazy('app_send_mail:message')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageCreateForm
    template_name = 'app_send_mail/message_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('app_send_mail:message')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('app_send_mail:message')


# ---------------------------------------------------------------- Логи --------------------------------

class LogsListView(ListView):
    model = Logs

