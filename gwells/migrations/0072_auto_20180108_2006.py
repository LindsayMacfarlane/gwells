# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-08 20:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0071_aquiferwell_aquifer_has_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aquiferwell',
            name='aquifer_has_report',
        ),
        migrations.RemoveField(
            model_name='well',
            name='observation_well_in_map_hub',
        ),
    ]