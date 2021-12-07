# Generated by Django 3.2.9 on 2021-12-07 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_apiuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='api_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='operations', to='main.apiuser', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operations1', to=settings.AUTH_USER_MODEL, verbose_name='User1'),
        ),
    ]
