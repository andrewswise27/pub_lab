import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Sausage Roll", 2.0, 1.0)
        self.food2 = Food("Pork Scratchings", 1.50, 0.6)
        self.food3 = Food("Bar Nuts", 0.10, 0.10)
    
    def test_food_has_name(self):
        self.assertEqual("Sausage Roll", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(2.0, self.food.price)

    def test_food_has_rejuvination_level(self):
        self.assertEqual(1.0, self.food.rejuvination_level)

    