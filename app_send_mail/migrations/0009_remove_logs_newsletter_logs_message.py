# Generated by Django 4.2.5 on 2023-10-12 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_send_mail', '0008_remove_logs_message_logs_newsletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logs',
            name='newsletter',
        ),
        migrations.AddField(
            model_name='logs',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_send_mail.newsletter', verbose_name='Сообщение'),
        ),
    ]