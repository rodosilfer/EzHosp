# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-27 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20170627_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostico',
            name='medico',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.Medico'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hospital',
            name='convenios',
            field=models.ManyToManyField(to='polls.Convenio'),
        ),
    ]