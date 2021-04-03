from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response
from ..models import Customer, Doctor
from reservation.utils import check_passowrd
from visit.serializers import *
from visit.application import RequestResponse
from rest_framework import status
from django.shortcuts import render, get_object_or_404


@api_view([('POST')])
def c_login(request):
    serializer = CustomerLoginSerializer(data=request.data)
    if serializer.is_valid():
        phone_num = serializer.validated_data['phone_num']
        password = serializer.validated_data['password']
        try:
            c = Customer.objects.get(phone_num=phone_num)
            if check_passowrd(password, c.password):
                return Response(CustomerGetSerializer(c).data)
            else:
                return JsonResponse(RequestResponse(False, "رمز ورود صحیح نیست").response_message())

        except Customer.DoesNotExist:
            return JsonResponse(RequestResponse(False, "این کاربر وجود ندارد").response_message())
    else:
        return JsonResponse(RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                            status=status.HTTP_400_BAD_REQUEST)


@api_view([('POST')])
def d_login(request):
    serializer = DoctorLoginSerializer(data=request.data)
    if serializer.is_valid():
        medical_num = serializer.validated_data['medical_num']
        password = serializer.validated_data['password']
        try:
            log = Doctor.objects.get(medical_num=medical_num)
            if check_passowrd(password, log.password):
                return Response(DoctorGetSerializer(log).data)
            else:
                return JsonResponse(RequestResponse(False, "رمز ورود صحیح نیست").response_message())

        except Doctor.DoesNotExist:
            return JsonResponse(RequestResponse(False, "این پزشک ثبت نام نکرده است").response_message())
    else:
        return JsonResponse(RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                            status=status.HTTP_400_BAD_REQUEST)


@api_view([('POST')])
def c_search_by_visittime(request):
    serializer = CustomerVisitSerializer(data=request.data)
    if serializer.is_valid():
        ds = serializer.validated_data['ds']
        de = serializer.validated_data['de']
        try:
            doctors = Doctor.objects.all()
            context = {
                'doctors': doctors,
            }
            if doctors:
                for doctor in doctors:
                    if doctor.working <= de and doctor.working >= ds:
                        serializer = DoctorGetSerializer(doctors, many=True)
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    else:
                        return JsonResponse(RequestResponse(False, "در این بازه ویزیت انجام نمیشود").response_message())
            else:
                return JsonResponse(RequestResponse(False, "پزشکی تاریخ ویزیت ثبت نکرده است").response_message())

        except Customer.DoesNotExist:
            return JsonResponse(RequestResponse(False, "پزشکی وجود ندارد").response_message())
    else:
        return JsonResponse(RequestResponse(False, "details : " + serializer.errors.__str__()).response_message(),
                            status=status.HTTP_400_BAD_REQUEST)


@api_view([('POST')])
def c_search_by_doctorname(request):
    doctors = Doctor.objects.all()
    if 'name' in request.POST:
        name = request.POST['name']
        doctors = doctors.filter(name=name)
    context = {
        'listings': doctors,
    }
    serializer = DoctorGetSerializer(doctors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
