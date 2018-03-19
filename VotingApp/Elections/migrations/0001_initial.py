# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-19 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elections',
            fields=[
                ('ElectionID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('AssociatedWith', models.CharField(max_length=50)),
                ('FromDate', models.DateField()),
                ('EndDate', models.DateField()),
            ],
        ),
    ]
