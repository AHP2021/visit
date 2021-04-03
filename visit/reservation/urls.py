from django.urls import path, include
from visit.application import BASE_API_ROOT

urlpatterns = [
    path(BASE_API_ROOT, include('reservation.api.urls')),
]
