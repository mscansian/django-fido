# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-27 09:27
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_fido', '0011_remove_credential_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='authenticator',
            name='label',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
