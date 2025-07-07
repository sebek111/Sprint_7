import pytest
import requests
import allure

BASE_URL = "https://qa-scooter.praktikum-services.ru"


@allure.epic("Курьеры")
@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_success(self, new_courier):
        payload = {
            "login": new_courier["login"],
            "password": new_courier["password"]
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Ошибка при неверном логине")
    def test_login_wrong_login(self):
        payload = {
            "login": "nonexistent_user",
            "password": "1234"
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Ошибка при неверном пароле")
    def test_login_wrong_password(self, new_courier):
        payload = {
            "login": new_courier["login"],
            "password": "wrongpass"
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Ошибка при отсутствии логина")
    def test_login_missing_login(self, new_courier):
        payload = {
            "password": new_courier["password"]
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Ошибка при отсутствии пароля")
    def test_login_missing_password(self, new_courier):
        payload = {
            "login": new_courier["login"]
        }
        response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

