import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Carling", 5.00)
        self.drink2 = Drink("Rosé", 7.50)

    def test_drink_has_name(self):
        self.assertEqual("Carling", self.drink.name)
    
    def test_drink_has_price(self):
        self.assertEqual(5.00, self.drink.price)
    
    
