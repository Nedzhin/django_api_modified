# Generated by Django 5.2.3 on 2025-07-04 03:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GPSurgery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'GP Surgeries',
            },
        ),
        migrations.CreateModel(
            name='InstructionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('AMRA', 'AMRA'), ('SARS', 'SARS'), ('POA', 'POA'), ('VAC', 'VACCINE')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surgery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.gpsurgery')),
            ],
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('gp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.gp')),
                ('surgery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.gpsurgery')),
                ('instruction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.instructiontype')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
