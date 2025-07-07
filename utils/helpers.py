import requests
import random
import string

BASE_URL = "https://qa-scooter.praktikum-services.ru"


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def register_new_courier_and_return_login_password():
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

    if response.status_code == 201:
        return [login, password, first_name]
    return []


def login_and_get_id(login, password):
    payload = {"login": login, "password": password}
    response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)
    return response.json().get("id")
