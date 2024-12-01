import pytest
from unittest.mock import Mock
from data import Data
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING



@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = Data.BUN_NAME
    mock_bun.get_price.return_value = Data.BUN_PRICE
    return mock_bun

@pytest.fixture()
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.get_price.return_value = Data.SAUCE_PRICE
    mock_sauce.get_name.return_value = Data.SAUCE_NAME
    mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_sauce

@pytest.fixture()
def mock_filling():
    mock_filling = Mock()
    mock_filling.get_price.return_value = Data.FILLING_PRICE
    mock_filling.get_name.return_value = Data.FILLING_NAME
    mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock_filling


