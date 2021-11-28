# Generated by Django 3.2.9 on 2021-11-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_categories_cat_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='cat_type',
            field=models.CharField(choices=[('EXP', 'Expense'), ('INC', 'Income')], default='EXP', max_length=3),
        ),
    ]
