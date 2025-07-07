import requests
import allure

BASE_URL = "https://qa-scooter.praktikum-services.ru"


@allure.epic("Заказы")
@allure.feature("Получение списка заказов")
class TestOrderList:

    @allure.title("Получение списка заказов")
    def test_get_order_list(self):
        response = requests.get(f"{BASE_URL}/api/v1/orders")

        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)
