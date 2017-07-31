# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-28 18:49
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0018_auto_20170727_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterPackMaterial',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('filter_pack_material_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_filter_pack_material',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='FilterPackMaterialSize',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('filter_pack_material_size_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_filter_pack_material_size',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('screen_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('screen_from', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='From')),
                ('screen_to', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='To')),
                ('internal_diameter', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(Decimal('0.0'))], verbose_name='Diameter')),
                ('slot_size', models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Slot Size')),
            ],
            options={
                'db_table': 'gwells_screen',
            },
        ),
        migrations.CreateModel(
            name='ScreenAssemblyType',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('screen_assembly_type_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_screen_assembly_type',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='ScreenBottom',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('screen_bottom_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_screen_bottom',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='ScreenIntake',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('screen_intake_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_screen_intake',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='ScreenMaterial',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('screen_material_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_screen_material',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='ScreenOpening',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('screen_opening_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_screen_opening',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.CreateModel(
            name='ScreenType',
            fields=[
                ('who_created', models.CharField(max_length=30)),
                ('when_created', models.DateTimeField(blank=True, null=True)),
                ('who_updated', models.CharField(max_length=30)),
                ('when_updated', models.DateTimeField(blank=True, null=True)),
                ('screen_type_guid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('is_hidden', models.BooleanField(default=False)),
                ('sort_order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gwells_screen_type',
                'ordering': ['sort_order', 'description'],
            },
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='filter_pack_from',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Filter Pack From'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='filter_pack_thickness',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Filter Pack Thickness'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='filter_pack_to',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Filter Pack To'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='other_screen_bottom',
            field=models.CharField(blank=True, max_length=50, verbose_name='Other Screen Bottom'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='other_screen_material',
            field=models.CharField(blank=True, max_length=50, verbose_name='Other Screen Material'),
        ),
        migrations.AddField(
            model_name='well',
            name='filter_pack_from',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Filter Pack From'),
        ),
        migrations.AddField(
            model_name='well',
            name='filter_pack_thickness',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Filter Pack Thickness'),
        ),
        migrations.AddField(
            model_name='well',
            name='filter_pack_to',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Filter Pack To'),
        ),
        migrations.AddField(
            model_name='well',
            name='other_screen_bottom',
            field=models.CharField(blank=True, max_length=50, verbose_name='Other Screen Bottom'),
        ),
        migrations.AddField(
            model_name='well',
            name='other_screen_material',
            field=models.CharField(blank=True, max_length=50, verbose_name='Other Screen Material'),
        ),
        migrations.AlterField(
            model_name='activitysubmission',
            name='liner_to',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Liner To'),
        ),
        migrations.AlterField(
            model_name='well',
            name='liner_to',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Liner To'),
        ),
        migrations.AddField(
            model_name='screen',
            name='activity_submission',
            field=models.ForeignKey(blank=True, db_column='filing_number', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ActivitySubmission'),
        ),
        migrations.AddField(
            model_name='screen',
            name='assembly_type',
            field=models.ForeignKey(blank=True, db_column='screen_assembly_type_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ScreenAssemblyType'),
        ),
        migrations.AddField(
            model_name='screen',
            name='well',
            field=models.ForeignKey(blank=True, db_column='well_tag_number', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.Well'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='filter_pack_material',
            field=models.ForeignKey(blank=True, db_column='filter_pack_material_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.FilterPackMaterial', verbose_name='Filter Pack Material'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='filter_pack_material_size',
            field=models.ForeignKey(blank=True, db_column='filter_pack_material_size_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.FilterPackMaterialSize', verbose_name='Filter Pack Material Size'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='screen_bottom',
            field=models.ForeignKey(blank=True, db_column='screen_bottom_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ScreenBottom', verbose_name='Screen Bottom'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='screen_intake',
            field=models.ForeignKey(blank=True, db_column='screen_intake_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ScreenIntake', verbose_name='Intake'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='screen_material',
            field=models.ForeignKey(blank=True, db_column='screen_material_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ScreenMaterial', verbose_name='Screen Material'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='screen_opening',
            field=models.ForeignKey(blank=True, db_column='screen_opening_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ScreenOpening', verbose_name='Screen Opening'),
        ),
        migrations.AddField(
            model_name='activitysubmission',
            name='screen_type',
            field=models.ForeignKey(blank=True, db_column='screen_type_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ScreenType', verbose_name='Screen Type'),
        ),
        migrations.AddField(
            model_name='well',
            name='filter_pack_material',
            field=models.ForeignKey(blank=True, db_column='filter_pack_material_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.FilterPackMaterial', verbose_name='Filter Pack Material'),
        ),
        migrations.AddField(
            model_name='well',
            name='filter_pack_material_size',
            field=models.ForeignKey(blank=True, db_column='filter_pack_material_size_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.FilterPackMaterialSize', verbose_name='Filter Pack Material Size'),
        ),
        migrations.AddField(
            model_name='well',
            name='screen_bottom',
            field=models.ForeignKey(blank=True, db_column='screen_bottom_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ScreenBottom', verbose_name='Screen Bottom'),
        ),
        migrations.AddField(
            model_name='well',
            name='screen_intake',
            field=models.ForeignKey(blank=True, db_column='screen_intake_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ScreenIntake', verbose_name='Intake'),
        ),
        migrations.AddField(
            model_name='well',
            name='screen_opening',
            field=models.ForeignKey(blank=True, db_column='screen_opening_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ScreenOpening', verbose_name='Screen Opening'),
        ),
        migrations.AddField(
            model_name='well',
            name='screen_type',
            field=models.ForeignKey(blank=True, db_column='screen_type_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.ScreenType', verbose_name='Screen Type'),
        ),
    ]