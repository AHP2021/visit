# Generated by Django 3.2.3 on 2021-05-13 09:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('text_body', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('phone_num', models.CharField(max_length=13, unique=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('medical_num', models.IntegerField(default=1)),
                ('phone_num', models.CharField(max_length=13, unique=True)),
                ('clinic_city', models.CharField(max_length=20)),
                ('degree', models.CharField(max_length=20)),
                ('working', models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 13, 13, 45, 49, 91351))),
                ('visible_do', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('specialty_id', models.AutoField(primary_key=True, serialize=False)),
                ('sp_name', models.CharField(max_length=60)),
                ('visible_sp', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'specialty',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('visit_id', models.AutoField(primary_key=True, serialize=False)),
                ('visit_date', models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 13, 13, 45, 49, 105389))),
                ('customer_id', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, to='reservation.customer')),
                ('doctor_id', models.ForeignKey(db_column='doctor_id', on_delete=django.db.models.deletion.CASCADE, to='reservation.doctor')),
            ],
            options={
                'db_table': 'visit',
            },
        ),
        migrations.CreateModel(
            name='ListVisit',
            fields=[
                ('list_visit_id', models.AutoField(primary_key=True, serialize=False)),
                ('doctor_id', models.ForeignKey(db_column='doctor_id', on_delete=django.db.models.deletion.CASCADE, to='reservation.doctor')),
                ('visit_id', models.ForeignKey(db_column='visit_id', on_delete=django.db.models.deletion.CASCADE, to='reservation.visit')),
            ],
            options={
                'db_table': 'listvisit',
            },
        ),
        migrations.CreateModel(
            name='ListComment',
            fields=[
                ('list_comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_id', models.ForeignKey(db_column='comment_id', on_delete=django.db.models.deletion.CASCADE, to='reservation.comment')),
                ('doctor_id', models.ForeignKey(db_column='doctor_id', on_delete=django.db.models.deletion.CASCADE, to='reservation.doctor')),
            ],
            options={
                'db_table': 'listcomment',
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty_id',
            field=models.ForeignKey(db_column='specialty_id', on_delete=django.db.models.deletion.CASCADE, to='reservation.specialty'),
        ),
        migrations.AddField(
            model_name='customer',
            name='fav_doc',
            field=models.ManyToManyField(blank=True, to='reservation.Doctor'),
        ),
        migrations.AddField(
            model_name='comment',
            name='customer_id',
            field=models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, to='reservation.customer'),
        ),
    ]
