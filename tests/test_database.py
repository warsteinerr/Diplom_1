import pytest
from data import DataBase
from praktikum.database import Database
import allure


class TestDatabase:

    @allure.title('Проверка получения списка булочек')
    @pytest.mark.parametrize('position, name, price', DataBase.BUNS_LIST)
    def test_available_buns(self,position, name, price):
        database = Database()
        buns = database.available_buns()
        assert buns[position].name == name and buns[position].price == price

    @allure.title('Проверка получения списка ингридиентов')
    @pytest.mark.parametrize('position, type, name, price', DataBase.INGRIDIENTS_LIST)
    def test_available_ingredients(self, position, type, name, price):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[position].name == name and ingredients[position].price == price and ingredients[position].type == type