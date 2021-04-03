from rest_framework import serializers
from reservation.api.models import *


# --------------- DOCTOR Serializer-------------
class DoctorGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('doctor_id', 'name', 'medical_num', 'phone_num', 'clinic_city',
                  'degree', 'working', 'specialty_id', 'visible_do')


class DoctorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name', 'medical_num', 'phone_num', 'clinic_city', 'degree', 'working', 'specialty_id'
                  , 'visible_do')


class DoctorPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('clinic_city', 'phone_num', 'working')


class DoctorLoginSerializer(serializers.Serializer):
    medical_num = serializers.IntegerField(default=1)
    password = serializers.CharField(max_length=100)


# -------------- END  DOCTOR  Serializer-------------

# -------------- LIST COMMENT Serializer--------------
class ListCommentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListComment
        fields = ('list_comment_id', 'comment_id', 'doctor_id')


class ListCommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListComment
        fields = ('comment_id', 'doctor_id')


# ------------END LIST COMMENT Serializer------------

# ------------LIST VISIT Serializer------------------
class ListVisitGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListVisit
        fields = ('list_visit_id', 'visit_id', 'doctor_id')


class ListVisitPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListVisit
        fields = ('visit_id', 'doctor_id')


# -----------END LIST VISIT Serializer-----------

# ---------VISIT Serializer----------------------
class VisitGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('visit_id', 'customer_id', 'doctor_id', 'visit_date')


class VisitPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('customer_id', 'doctor_id', 'visit_date')


# ---------END VISIT Serializer-----------------

# ---------COMMENT Serializer-------------------
class CommentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_id', 'customer_id', 'text_body')


class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('customer_id', 'text_body')


# ---------END COMMENT Serializer -----------------

# -----------Specialty Serializer----------
class SpecialtyGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ('specialty_id', 'sp_name', 'visible_sp')


class SpecialtyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ('sp_name', 'visible_sp')


# -------- END Specialty Serializer-------------------

# --------------- CUSTOMER Serializer-------------

class CustomerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id', 'name', 'phone_num', 'fav_doc')


class CustomerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'phone_num', 'fav_doc')


class CustomerLoginSerializer(serializers.Serializer):
    phone_num = serializers.CharField(max_length=13)
    password = serializers.CharField(max_length=100)


class CustomerVisitSerializer(serializers.Serializer):
    ds = serializers.DateTimeField(default=datetime.now())
    de = serializers.DateTimeField(default=datetime.now())


# -------------- END  CUSTOMER  Serializer-------------
