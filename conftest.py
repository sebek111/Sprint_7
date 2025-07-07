import pytest
import requests
from utils.helpers import generate_random_string, login_and_get_id

BASE_URL = "https://qa-scooter.praktikum-services.ru"


@pytest.fixture
def new_courier():
    """Фикстура: создаёт нового курьера и удаляет его после теста."""
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)
    assert response.status_code == 201, f"Не удалось создать курьера: {response.text}"

    courier_id = login_and_get_id(login, password)
    yield {
        "login": login,
        "password": password,
        "first_name": first_name,
        "id": courier_id
    }

    if courier_id:
        requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")
