# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-14 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_consulta'),
    ]

    operations = [
        migrations.CreateModel(
            name='GerenciarExame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.ManyToManyField(to='polls.Hospital')),

            ],
        ),
        migrations.AddField(
            model_name='exame',
            name='hospital',
            field=models.ManyToManyField(to='polls.Hospital'),
        ),
        migrations.AddField(
            model_name='exame',
            name='paciente',
            field=models.ManyToManyField(to='polls.Patient'),
        ),
    ]
