# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_placephoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('persons', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('wish', models.CharField(max_length=300)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app.Client')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RequestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('text', models.CharField(max_length=300)),
                ('recommendation', models.BooleanField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Order')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='app.RequestType'),
        ),
    ]
