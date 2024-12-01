from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
class Data:
    BUN_NAME = 'black bun'
    BUN_PRICE = 100
    SAUCE_PRICE = 200
    FILLING_PRICE = 200
    SAUCE_NAME = 'sour cream'
    FILLING_NAME = 'dinosaur'
    BURGER_SUM = BUN_PRICE*2 + SAUCE_PRICE + FILLING_PRICE

class DataBase:

	BUNS_LIST = [
        [0, 'black bun', 100],
        [1, 'white bun', 200],
        [2, 'red bun', 300]
    ]

	INGRIDIENTS_LIST = [
		[0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100],
		[1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200],
		[2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300],
		[3, INGREDIENT_TYPE_FILLING, 'cutlet', 100],
		[4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200],
		[5, INGREDIENT_TYPE_FILLING, 'sausage', 300]

]


