# Generated by Django 3.2.9 on 2021-12-07 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_rename_api_user_operation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operations', to='main.apiuser', verbose_name='User'),
        ),
    ]
