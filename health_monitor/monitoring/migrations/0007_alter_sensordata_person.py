# Generated by Django 5.1.7 on 2025-03-12 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0006_person_sensordata_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='monitoring.person'),
        ),
    ]
