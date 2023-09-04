from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Clients(models.Model):
    name = models.CharField(max_length=25, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    sur_name = models.CharField(max_length=50, verbose_name='Отчество')
    email = models.EmailField(max_length=100, verbose_name='Почта')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.name} {self.last_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Newsletter(models.Model):
    time = models.DateTimeField(**NULLABLE, verbose_name='Время')
    periodicity = models.DurationField(verbose_name='Периодичность')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.time} {self.periodicity}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тема письма')
    content = models.TextField(**NULLABLE, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.title} {self.content}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Logs(models.Model):
    time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')
    attempt_status = models.IntegerField(verbose_name='Cтатус рассылки')
    answer = models.BooleanField(default=False, verbose_name='Ответ почтового сервера')

    def __str__(self):
        return f'{self.time}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
