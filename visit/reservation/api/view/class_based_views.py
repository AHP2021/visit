from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reservation.api.models import *
from visit.serializers import *
from django.http import JsonResponse
from visit.application import RequestResponse


#  ---------------------DOCTOR VIEW-----------------
class DoctorView(APIView):

    def get(self, *args, **kwargs):
        specialty_id = self.request.query_params.get('specialty_id', None)
        global doctor
        if specialty_id is not None:
            doctor = Doctor.objects.filter(specialty_id=specialty_id)
        else:
            doctor = Doctor.objects.all()
        serializer = DoctorGetSerializer(doctor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        serializer = DoctorPostSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(RequestResponse(True, "مشخصات پزشک با موفقیت ثبت شد").response_message()
                                )
        else:
            return JsonResponse(RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                                )

    def put(self, request, doctor_id):
        global dr
        try:
            dr = Doctor.objects.get(doctor_id=doctor_id)
        except Doctor.DoesNotExist:
            return JsonResponse(RequestResponse(False, "پزشک قبلا ثبت نشده است").response_message())

        else:
            serializer = DoctorPutSerializer(dr, data=request.data)
            if serializer.is_valid():
                dr.save()
                return JsonResponse(RequestResponse(True, " مشخصات پزشک با موفقیت ویرایش شد").response_message()
                                    , status=status.HTTP_200_OK)
            else:
                return JsonResponse(
                    RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                    status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, doctor_id):
        try:
            doctor = Doctor.objects.get(doctor_id=doctor_id)
            doctor.delete()
            return JsonResponse(RequestResponse(True, "پزشک حذف شد").response_message())

        except Doctor.DoesNotExist:
            return JsonResponse(
                RequestResponse(False, "در خواست غیر مجاز").response_message(),
                status=status.HTTP_400_BAD_REQUEST)


#  -----------------END DOCTOR VIEW----------------------

#  -----------------LIST COMMENT VIEW--------------------

class ListCommentView(APIView):

    def get(self, *args, **kwargs):
        listcomment = ListComment.objects.all()
        serializer = ListCommentGetSerializer(listcomment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ListCommentPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(RequestResponse(True, "ثبت لیست کامنت انجام شد").response_message()
                                , status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, list_comment_id):
        global listcomment
        try:
            listcomment = ListComment.objects.get(list_comment_id=list_comment_id)
        except ListComment.DoesNotExist:
            return JsonResponse(RequestResponse(False, "کامنت وجود ندارد").response_message())

        else:
            serializer = ListCommentPostSerializer(listcomment, data=request.data)
            if serializer.is_valid():
                listcomment.save()
                return JsonResponse(RequestResponse(True, "لیست کامنت تغییر کرد").response_message()
                                    , status=status.HTTP_200_OK)
            else:
                return JsonResponse(
                    RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                    status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, list_comment_id):
        try:
            listcomment = ListComment.objects.get(list_comment_id=list_comment_id)
            listcomment.delete()
            return JsonResponse(RequestResponse(True, "لیست کامنت حذف شد").response_message())
        except Comment.DoesNotExist:
            return JsonResponse(
                RequestResponse(False, "در خواست غیر مجاز").response_message(),
                status=status.HTTP_400_BAD_REQUEST)


#  -----------------END LIST COMMENT VIEW----------------

# ------------------LIST VISIT VIEW----------------------
class ListVisitView(APIView):

    def get(self, *args, **kwargs):
        listvisit = ListVisit.objects.all()
        serializer = ListVisitGetSerializer(listvisit, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ListVisitPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(RequestResponse(True, "ثبت لیست ویزیت انجام شد").response_message()
                                , status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, list_visit_id):
        global listvisit
        try:
            listvisit = ListVisit.objects.get(list_visit_id=list_visit_id)
        except ListVisit.DoesNotExist:
            return JsonResponse(RequestResponse(False, "این ملاقات ها وجود ندارد").response_message())

        else:
            serializer = ListVisitPostSerializer(listvisit, data=request.data)
            if serializer.is_valid():
                listvisit.save()
                return JsonResponse(RequestResponse(True, "لیست ملاقات تغییر کرد").response_message()
                                    , status=status.HTTP_200_OK)
            else:
                return JsonResponse(
                    RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                    status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, list_visit_id):
        try:
            listvisit = ListVisit.objects.get(list_visit_id=list_visit_id)
            listvisit.delete()
            return JsonResponse(RequestResponse(True, "لیست ملاقات حذف شد").response_message())
        except Visit.DoesNotExist:
            return JsonResponse(
                RequestResponse(False, "در خواست غیر مجاز").response_message(),
                status=status.HTTP_400_BAD_REQUEST)


# ------------------END LIST VISIT VIEW------------------

# ------------------COMMENT VIEW------------------------

class Commentview(APIView):
    def get(self, *args, **kwargs):
        comment = Comment.objects.all()
        serializer = CommentGetSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = CommentPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(RequestResponse(True,
                                                str(serializer.validated_data['customer_id'] +
                                                    'کامنت توسط کاربر با شناسه:')).response_message()
                                , status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, comment_id):
        global comment
        try:
            comment = Comment.objects.get(comment_id=comment_id)
        except Comment.DoesNotExist:
            return JsonResponse(RequestResponse(False, "این کامنت وجود ندارد").response_message())

        else:
            serializer = CommentPostSerializer(comment, data=request.data)
            if serializer.is_valid():
                comment.save()
                return JsonResponse(RequestResponse(True, "کامنت تغییر کرد").response_message()
                                    , status=status.HTTP_200_OK)
            else:
                return JsonResponse(
                    RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                    status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id):
        try:
            comment = Comment.objects.get(comment_id=comment_id)
            comment.delete()
            return JsonResponse(RequestResponse(True, "کامنت حدف شد").response_message())
        except Comment.DoesNotExist:
            return JsonResponse(
                RequestResponse(False, "در خواست غیر مجاز").response_message(),
                status=status.HTTP_400_BAD_REQUEST)


# ----------------END COMMENT VIEW-------------------------------

# ----------------VISIT VIEW-------------------------------------

class Visitview(APIView):
    def get(self, *args, **kwargs):
        visit = Visit.objects.all()
        serializer = VisitGetSerializer(visit, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = VisitPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(RequestResponse(True,
                                                str(serializer.validated_data['customer_id'] +
                                                    'درخواست ملاقات توسط کاربر با شناسه:')).response_message()
                                , status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, visit_id):
        global visit
        try:
            visit = Visit.objects.get(visit_id=visit_id)
        except Visit.DoesNotExist:
            return JsonResponse(RequestResponse(False, "این قرار ملاقات وجود ندارد").response_message())

        else:
            serializer = VisitPostSerializer(visit, data=request.data)
            if serializer.is_valid():
                visit.save()
                return JsonResponse(RequestResponse(True, "قرار ملاقات تغییر کرد").response_message()
                                    , status=status.HTTP_200_OK)
            else:
                return JsonResponse(
                    RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                    status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, visit_id):
        try:
            visit = Visit.objects.get(visit_id=visit_id)
            visit.delete()
            return JsonResponse(RequestResponse(True, "قرار ملاقات حدف شد").response_message())
        except Visit.DoesNotExist:
            return JsonResponse(
                RequestResponse(False, "در خواست غیر مجاز").response_message(),
                status=status.HTTP_400_BAD_REQUEST)


#
# --------------END VISIT VIEW---------------------------

# --------------SPECIALTY VIEW---------------------------

class SpecialtyView(APIView):

    def get(self, *args, **kwargs):
        specialty = Specialty.objects.all()
        serializer = SpecialtyGetSerializer(specialty, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SpecialtyPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(RequestResponse(True, "ثبت تخصص انجام شد").response_message()
                                , status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, specialty_id):
        global sp
        try:
            sp = Specialty.objects.get(specialty_id=specialty_id)
        except Specialty.DoesNotExist:
            return JsonResponse(RequestResponse(False, "تخصص وجود ندارد").response_message())

        else:
            serializer = SpecialtyPostSerializer(sp, data=request.data)
            if serializer.is_valid():
                sp.save()
                return JsonResponse(RequestResponse(True, "تخصص تغییر کرد").response_message()
                                    , status=status.HTTP_200_OK)
            else:
                return JsonResponse(
                    RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                    status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, specialty_id):
        try:
            spc = Specialty.objects.get(specialty_id=specialty_id)
            spc.delete()
            return JsonResponse(RequestResponse(True, "تخصص حذف شد").response_message())
        except Specialty.DoesNotExist:
            return JsonResponse(
                RequestResponse(False, "در خواست غیر مجاز").response_message(),
                status=status.HTTP_400_BAD_REQUEST)


# --------------END SPECIALTY VIEW-----------------------

#  ---------------------CUSTOMER VIEW-----------------
class CustomerView(APIView):

    def get(self, *args, **kwargs):
        customer = Customer.objects.all()
        serializer = CustomerGetSerializer(customer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        serializer = CustomerPostSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(RequestResponse(True, "مشخصات کاربر با موفقیت ثبت شد").response_message()
                                )
        else:
            return JsonResponse(RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                                )

    def put(self, request, customer_id):
        global customer
        try:
            customer = Customer.objects.get(customer_id=customer_id)
        except Customer.DoesNotExist:
            return JsonResponse(RequestResponse(False, "کاربر قبلا ثبت نشده است").response_message())

        else:
            serializer = CustomerPostSerializer(customer, data=request.data)
            if serializer.is_valid():
                customer.save()
                return JsonResponse(RequestResponse(True, " مشخصات کاربر با موفقیت ویرایش شد").response_message()
                                    , status=status.HTTP_200_OK)
            else:
                return JsonResponse(
                    RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                    status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, customer_id):
        try:
            customer = Customer.objects.get(customer_id=customer_id)
            customer.delete()
            return JsonResponse(RequestResponse(True, "کاربر حذف شد").response_message())

        except Customer.DoesNotExist:
            return JsonResponse(
                RequestResponse(False, "در خواست غیر مجاز").response_message(),
                status=status.HTTP_400_BAD_REQUEST)

#  -----------------END CUSTOMER VIEW----------------------
