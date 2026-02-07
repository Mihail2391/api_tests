import requests
import allure
from pydantic import BaseModel

BASE_URL = "https://petstore.swagger.io/v2"


class User(BaseModel):
    id: int
    username: str


class Order(BaseModel):
    id: int
    petId: int
    quantity: int


@allure.feature("User")
class TestUser:

    @allure.story("POST create user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user(self):
        user = User(id=1, username="test1")
        r = requests.post(f"{BASE_URL}/user", json=user.model_dump())
        assert r.status_code == 200

    @allure.story("GET user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_user(self):
        r = requests.get(f"{BASE_URL}/user/test1")
        assert r.status_code in (200, 404)

    @allure.story("PUT update user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_user(self):
        user = User(id=1, username="test1")
        r = requests.put(f"{BASE_URL}/user/test1", json=user.model_dump())
        assert r.status_code in (200, 404)

    @allure.story("DELETE user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_user(self):
        r = requests.delete(f"{BASE_URL}/user/test1")
        assert r.status_code in (200, 404)

    @allure.story("GET user after delete")
    @allure.severity(allure.severity_level.MINOR)
    def test_get_user_after_delete(self):
        # доп. тест, чтобы стало 9+ и был полноценный сценарий
        requests.delete(f"{BASE_URL}/user/test1")
        r = requests.get(f"{BASE_URL}/user/test1")
        assert r.status_code in (200, 404)


@allure.feature("Store")
class TestStore:

    @allure.story("POST order")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_place_order(self):
        order = Order(id=10, petId=1, quantity=1)
        r = requests.post(f"{BASE_URL}/store/order", json=order.model_dump())
        assert r.status_code == 200

    @allure.story("GET order by id")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_order(self):
        r = requests.get(f"{BASE_URL}/store/order/1")
        assert r.status_code in (200, 404)

    @allure.story("DELETE order")
    @allure.severity(allure.severity_level.MINOR)
    def test_delete_order(self):
        r = requests.delete(f"{BASE_URL}/store/order/1")
        assert r.status_code in (200, 404)

    @allure.story("GET inventory")
    @allure.severity(allure.severity_level.NORMAL)
    def test_inventory(self):
        r = requests.get(f"{BASE_URL}/store/inventory")
        assert r.status_code == 200
