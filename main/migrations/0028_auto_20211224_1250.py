# Generated by Django 3.2.9 on 2021-12-24 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20211224_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apiuser',
            name='date_filter_end',
        ),
        migrations.RemoveField(
            model_name='apiuser',
            name='date_filter_start',
        ),
        migrations.RemoveField(
            model_name='apiuser',
            name='pin_message_id',
        ),
    ]
