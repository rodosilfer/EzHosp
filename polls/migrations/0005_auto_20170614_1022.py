# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170614_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exame',
            name='hospital',
        ),
        migrations.AddField(
            model_name='exame',
            name='hospital',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.Hospital'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='exame',
            name='paciente',
        ),
        migrations.AddField(
            model_name='exame',
            name='paciente',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.Patient'),
            preserve_default=False,
        ),




    ]
