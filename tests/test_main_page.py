import json
from utils.main_page.api import get_active_items, get_cart, add_to_cart
import allure
from utils.functions import attach_regress

@allure.parent_suite('Главная страница')
@allure.suite('Проверка добавления товара в Корзину у незарегистрированного пользователя')
@allure.title("Получение товаров")
def test_get_active_items():
    global offer_id, slug, condition_id

    with allure.step('Отправка запроса на получение товаров'):
        response = get_active_items()
        attach_regress(response=response)

    with allure.step('Проверка статуса ответа'):
        assert response.status_code == 200

    response = response.json()

    with allure.step('Проверка что в ответе есть товары'):
        assert len(response) > 0

    first_item = response[0]["offers"][0]

    offer_id = first_item["moderated_offer_id"]
    slug = first_item["slug"]
    condition_id = first_item["condition"]["id"]


@allure.parent_suite('Главная страница')
@allure.suite('Проверка добавления товара в Корзину у незарегистрированного пользователя')
@allure.title("Получение session_id из куки")
def test_get_session_id():
    global cookie

    with allure.step('Отправка запроса на получение корзины'):
        response = get_cart()
        attach_regress(response=response)

    with allure.step('Проверка статуса ответа'):
        assert response.status_code == 200

    with allure.step('Получение session_id из куки'):
        cookie = response.cookies.get_dict().get('cart')
        assert cookie, "cookie 'cart' пустая или отсутствует"
        assert isinstance(cookie, (str, int)), f'Ожидали str или int, но получили {type(cookie)}'


@allure.parent_suite('Главная страница')
@allure.suite('Проверка добавления товара в Корзину у незарегистрированного пользователя')
@allure.title("Добавление товара в корзину")
def test_add_item():
    response = add_to_cart(cookie=cookie, offer_id=offer_id, condition_id=condition_id)
    attach_regress(response=response)

    assert response.status_code == 200

    response = response.json()
    print(json.dumps(response, indent=4))