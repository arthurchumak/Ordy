# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=5)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='app.Currency')),
            ],
        ),
    ]
