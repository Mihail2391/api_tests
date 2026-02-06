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
    def test_create_user(self):
        user = User(id=1, username="test1")
        r = requests.post(f"{BASE_URL}/user", json=user.model_dump())
        assert r.status_code == 200

    @allure.story("GET user")
    def test_get_user(self):
        r = requests.get(f"{BASE_URL}/user/test1")
        assert r.status_code in (200, 404)

    @allure.story("DELETE user")
    def test_delete_user(self):
        r = requests.delete(f"{BASE_URL}/user/test1")
        assert r.status_code in (200, 404)


@allure.feature("Store")
class TestStore:

    @allure.story("POST order")
    def test_place_order(self):
        order = Order(id=10, petId=1, quantity=1)
        r = requests.post(f"{BASE_URL}/store/order", json=order.model_dump())
        assert r.status_code == 200

    @allure.story("GET inventory")
    def test_inventory(self):
        r = requests.get(f"{BASE_URL}/store/inventory")
        assert r.status_code == 200
