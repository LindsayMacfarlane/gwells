# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-13 20:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0021_auto_20171113_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linermaterial',
            old_name='code',
            new_name='liner_material_code',
        ),
    ]
