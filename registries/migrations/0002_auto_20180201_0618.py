# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-01 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactat',
            name='contact_tel',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Contact telephone number'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='fax_tel',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Facsimile telephone number'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='main_tel',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Company main telephone number'),
        ),
    ]