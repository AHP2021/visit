# Generated by Django 3.1.7 on 2021-04-03 10:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_auto_20210328_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='working',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 3, 14, 30, 18, 589339)),
        ),
        migrations.AlterField(
            model_name='visit',
            name='visit_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 3, 14, 30, 18, 601347)),
        ),
    ]
