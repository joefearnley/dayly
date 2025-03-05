# Generated by Django 5.1.5 on 2025-03-05 00:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_remove_title_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='date_updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date updated'),
        ),
    ]
