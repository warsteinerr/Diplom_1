import allure
from praktikum.bun import Bun
import pytest
from data import Data


class TestBun:

    @allure.title('Проверка инициализации булки')
    def test_initial(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert bun.name == Data.BUN_NAME and bun.price == Data.BUN_PRICE

    @allure.title('Проверка имени булки')
    def test_get_name(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert bun.get_name() == Data.BUN_NAME

    @allure.title('Проверка цены булки')
    def test_get_price(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert bun.get_price() == Data.BUN_PRICE

