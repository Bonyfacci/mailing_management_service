# Generated by Django 4.2.5 on 2023-09-25 18:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('sur_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=100, verbose_name='Почта')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ('last_name',),
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки')),
                ('attempt_status', models.CharField(choices=[('success', 'Успешно'), ('error', 'Ошибка')], max_length=20, verbose_name='Статус отправки')),
                ('server_response', models.TextField(blank=True, null=True, verbose_name='Ответ сервера')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тема письма')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.datetime_safe.datetime.now, verbose_name='Время')),
                ('start', models.DateTimeField(default=django.utils.datetime_safe.datetime.now, verbose_name='Начало времени')),
                ('finish', models.DateTimeField(default=django.utils.datetime_safe.datetime.now, verbose_name='Конец времени')),
                ('periodicity', models.CharField(choices=[('Один раз', 'Один раз'), ('Раз в день', 'Раз в день'), ('Раз в неделю', 'Раз в неделю'), ('Раз в месяц', 'Раз в месяц')], max_length=150, verbose_name='Периодичность')),
                ('status', models.CharField(choices=[('Создана', 'Создана'), ('Завершена', 'Завершена'), ('Запущена', 'Запущена')], default='Создана', max_length=100, verbose_name='Статус')),
                ('client_id', models.ManyToManyField(to='app_send_mail.client', verbose_name='id Клиента')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_send_mail.message', verbose_name='message')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
    ]
