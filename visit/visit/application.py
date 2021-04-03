from rest_framework.permissions import BasePermission

BASE_API_ROOT = 'api/'


class RequestResponse:
    def __init__(self, is_successful, message):
        self.is_successful = is_successful
        self.message = message

    def response_message(self):
        return {"is_successful": self.is_successful, "message": self.message}


class Authenticate(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
