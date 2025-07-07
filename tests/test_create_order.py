import requests
import allure
import pytest

BASE_URL = "https://qa-scooter.praktikum-services.ru"


@allure.epic("Заказы")
@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с разными вариантами цвета")
    @pytest.mark.parametrize("colors", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_colors(self, colors):
        payload = {
            "firstName": "Тест",
            "lastName": "Пользователь",
            "address": "Москва, улица Пушкина, д. 1",
            "metroStation": 4,
            "phone": "+7 999 999 99 99",
            "rentTime": 5,
            "deliveryDate": "2025-07-06",
            "comment": "Проверь заказ",
            "color": colors
        }

        response = requests.post(f"{BASE_URL}/api/v1/orders", json=payload)

        assert response.status_code == 201
        assert "track" in response.json()
