from django.contrib.auth.hashers import make_password, check_password
from visit.settings import BASE_DIR


def hash_password(password):
    return make_password(password)


def check_passowrd(raw_password, hashed_password):
    return check_password(raw_password, hashed_password)
