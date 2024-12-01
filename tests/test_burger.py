import allure
from praktikum.burger import Burger
import pytest
from data import Data


class TestBurger:

    @allure.title('Проверка инициализации булки и ингридиентов в бургере')
    def test_burger_init(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    @allure.title('Проверка установки булки')
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title('Проверка установки ингридиентов')
    def test_add_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        assert mock_sauce in burger.ingredients

    @allure.title('Проверка удаления ингридиентов')
    def test_remove_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)
        assert mock_sauce not in burger.ingredients

    @allure.title('Проверка смещения ингридиентов')
    def test_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(1,0)
        assert burger.ingredients[0] == mock_filling

    @allure.title('Проверка цены бургера')
    def test_get_price(self, mock_sauce, mock_bun, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_price() == Data.BURGER_SUM

    @allure.title('Проверка чека бургера')
    def test_get_receipt(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_receipt() == (
            f"(==== black bun ====)\n"
            f"= sauce sour cream =\n"
            f"= filling dinosaur =\n"
            f"(==== black bun ====)\n\n"
            f"Price: {burger.get_price()}"
        )





