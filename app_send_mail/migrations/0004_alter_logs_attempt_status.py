# Generated by Django 4.2.5 on 2023-10-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_send_mail', '0003_remove_newsletter_finish_remove_newsletter_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='attempt_status',
            field=models.CharField(choices=[('OK', 'Успешно'), ('ERROR', 'Ошибка')], max_length=20, verbose_name='Статус отправки'),
        ),
    ]
