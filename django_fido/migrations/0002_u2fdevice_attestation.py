# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-24 14:03
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_fido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='u2fdevice',
            name='attestation',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
