# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-27 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_remove_exame_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exame',
            name='horario',
            field=models.DateTimeField(verbose_name='%d-%m-%Y %H:%M'),
        ),
    ]
