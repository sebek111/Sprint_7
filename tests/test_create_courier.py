import requests
import allure
from utils.helpers import generate_random_string, login_and_get_id

BASE_URL = "https://qa-scooter.praktikum-services.ru"


@allure.epic("Курьеры")
@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        login = generate_random_string()
        password = generate_random_string()
        first_name = generate_random_string()
        payload = {"login": login, "password": password, "firstName": first_name}

        response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

        assert response.status_code == 201
        assert response.json()["ok"] is True

        courier_id = login_and_get_id(login, password)
        requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, new_courier):
        payload = {
            "login": new_courier["login"],
            "password": new_courier["password"],
            "firstName": new_courier["first_name"]
        }

        response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Ошибка при отсутствии обязательного поля 'password'")
    def test_create_courier_missing_password(self):
        payload = {
            "login": generate_random_string(),
            "firstName": generate_random_string()
        }

        response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Ошибка при отсутствии обязательного поля 'login'")
    def test_create_courier_missing_login(self):
        payload = {
            "password": generate_random_string(),
            "firstName": generate_random_string()
        }

        response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Ошибка при отсутствии всех обязательных полей")
    def test_create_courier_missing_all(self):
        payload = {}

        response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

