# Generated by Django 4.2.5 on 2023-10-10 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_send_mail', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='finish',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='start',
        ),
    ]
