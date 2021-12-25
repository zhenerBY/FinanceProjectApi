# Generated by Django 3.2.9 on 2021-12-24 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_category_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiuser',
            name='date_filter_end',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Date filter end'),
        ),
        migrations.AddField(
            model_name='apiuser',
            name='date_filter_start',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Date filter start'),
        ),
        migrations.AddField(
            model_name='apiuser',
            name='pin_message_id',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Pinned message id'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operations', to='main.category', verbose_name='Category'),
        ),
    ]
