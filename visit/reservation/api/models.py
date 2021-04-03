from django.db import models
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings
from datetime import datetime


class Specialty(models.Model):
    specialty_id = models.AutoField(primary_key=True)
    sp_name = models.CharField(max_length=60)
    visible_sp = models.BooleanField(default=True)

    class Meta:
        db_table = 'specialty'


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    medical_num = models.IntegerField(default=1)
    phone_num = models.CharField(max_length=13, unique=True)
    clinic_city = models.CharField(max_length=20)
    degree = models.CharField(max_length=20)
    working = models.DateTimeField(blank=True, default=datetime.now())
    specialty_id = models.ForeignKey('Specialty', on_delete=models.CASCADE, db_column='specialty_id')
    visible_do = models.BooleanField(default=True)

    class Meta:
        db_table = 'doctor'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    phone_num = models.CharField(max_length=13, unique=True)
    fav_doc = models.ManyToManyField(Doctor, blank=True)

    class Meta:
        db_table = 'customer'


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE, db_column='customer_id')
    text_body = models.TextField(blank=True)

    class Meta:
        db_table = 'comment'


class ListComment(models.Model):
    list_comment_id = models.AutoField(primary_key=True)
    comment_id = models.ForeignKey('Comment', on_delete=models.CASCADE, db_column='comment_id')
    doctor_id = models.ForeignKey('Doctor', on_delete=models.CASCADE, db_column='doctor_id')

    class Meta:
        db_table = 'listcomment'


class Visit(models.Model):
    visit_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE, db_column='customer_id')
    doctor_id = models.ForeignKey('Doctor', on_delete=models.CASCADE, db_column='doctor_id')
    visit_date = models.DateTimeField(blank=True, default=datetime.now())

    class Meta:
        db_table = 'visit'


class ListVisit(models.Model):
    list_visit_id = models.AutoField(primary_key=True)
    visit_id = models.ForeignKey('Visit', on_delete=models.CASCADE, db_column='visit_id')
    doctor_id = models.ForeignKey('Doctor', on_delete=models.CASCADE, db_column='doctor_id')

    class Meta:
        db_table = 'listvisit'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
