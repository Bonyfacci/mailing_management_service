# Generated by Django 4.2.5 on 2023-10-12 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_send_mail', '0005_alter_logs_attempt_status_alter_logs_send_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logs',
            options={'ordering': ('send_time',), 'verbose_name': 'Лог', 'verbose_name_plural': 'Логи'},
        ),
    ]
