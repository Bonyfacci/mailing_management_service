from django.conf import settings
from django.db import models
from django.utils.datetime_safe import datetime

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    name = models.CharField(max_length=25, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    sur_name = models.CharField(max_length=50, verbose_name='Отчество', **NULLABLE)
    email = models.EmailField(max_length=100, verbose_name='Почта')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('last_name',)


class Message(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тема письма')
    content = models.TextField(**NULLABLE, verbose_name='Комментарий')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Newsletter(models.Model):

    ONCE = 'Один раз'
    DAILY = 'Раз в день'
    WEEKLY = 'Раз в неделю'
    MONTHLY = 'Раз в месяц'

    PERIODICITY = [
        (ONCE, 'Один раз'),
        (DAILY, 'Раз в день'),
        (WEEKLY, 'Раз в неделю'),
        (MONTHLY, 'Раз в месяц'),
    ]

    CREATED = 'Создана'
    COMPLETED = 'Завершена'
    ACTIVE = 'Запущена'

    SELECT_STATUS = [
        (CREATED, 'Создана'),
        (COMPLETED, 'Завершена'),
        (ACTIVE, 'Запущена'),
    ]

    client_id = models.ManyToManyField(Client, verbose_name='id Клиента')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='message')

    time = models.DateTimeField(default=datetime.now, verbose_name='Время')
    periodicity = models.CharField(max_length=150, choices=PERIODICITY, verbose_name='Периодичность')
    status = models.CharField(max_length=100, default='Создана', choices=SELECT_STATUS, verbose_name='Статус')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return f"{self.message} {self.start} {self.periodicity}"

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Logs(models.Model):

    STATUS = (
        ('success', 'Успешно'),
        ('error', 'Ошибка'),
    )

    message = models.ForeignKey(Newsletter, on_delete=models.CASCADE, **NULLABLE, verbose_name='Сообщение')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, **NULLABLE, verbose_name='Клиент')
    send_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки')
    attempt_status = models.CharField(max_length=20, choices=STATUS, verbose_name='Статус отправки')
    server_response = models.TextField(**NULLABLE, verbose_name='Ответ сервера')

    def __str__(self):
        return f'{self.message} {self.send_time}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
