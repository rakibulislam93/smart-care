# Generated by Django 5.0.6 on 2024-07-09 06:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
        ('doctor', '0005_alter_reviewmodel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentmodel',
            name='appointment_status',
            field=models.CharField(choices=[('Complete', 'Complete'), ('Pending', 'Pending'), ('Running', 'Running')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='appointmentmodel',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.availabletime'),
        ),
    ]
