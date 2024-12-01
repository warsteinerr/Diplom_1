import allure
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import Data
import pytest


class TestIngredient:

    @allure.title('Проверка метода получения цены ингридента')
    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_NAME, Data.SAUCE_PRICE)
        assert ingredient.get_price() == ingredient.price

    @allure.title('Проверка метода получения имени ингридента')
    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_NAME, Data.SAUCE_PRICE)
        assert ingredient.get_name() == ingredient.name

    @allure.title('Проверка метода получения типа ингридента')
    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.SAUCE_NAME, Data.SAUCE_PRICE)
        assert ingredient.get_type() == ingredient.type

