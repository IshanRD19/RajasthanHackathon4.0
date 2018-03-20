# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-20 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('MiddleName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Picture', models.ImageField(default=b'Candidate_Pics/None/no_image.jpg', upload_to=b'Candidate_Pics/')),
                ('Sex', models.CharField(max_length=12)),
                ('DOB', models.DateField()),
                ('Contact', models.CharField(max_length=12)),
                ('RepresentativeOf', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='IdDetectionAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_proof', models.ImageField(upload_to=b'media/')),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('ArUcoID', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=30)),
                ('MiddleName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=30)),
                ('SSN', models.CharField(max_length=12)),
                ('Picture', models.ImageField(default=b'Voter_Pics/None/no_image.jpg', upload_to=b'Voter_Pics/')),
                ('DOB', models.DateField()),
                ('Sex', models.CharField(max_length=12)),
                ('Contact', models.CharField(max_length=12)),
                ('Address', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=30)),
                ('Pincode', models.CharField(max_length=6)),
            ],
        ),
    ]
