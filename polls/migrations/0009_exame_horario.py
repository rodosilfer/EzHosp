# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_diagnostico'),
    ]

    operations = [
        migrations.AddField(
            model_name='exame',
            name='horario',
            field=models.DateTimeField(default='1111-11-11 11:11'),
            preserve_default=False,
        ),
    ]