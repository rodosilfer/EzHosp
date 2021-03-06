# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-26 22:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170626_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField()),
                ('diagnostico', models.CharField(max_length=100)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField()),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='ModeloExame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Hospital')),
            ],
        ),
        migrations.AddField(
            model_name='exame',
            name='nome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.ModeloExame'),
        ),
        migrations.AddField(
            model_name='exame',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Paciente'),
        ),
    ]
