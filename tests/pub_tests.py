from unicodedata import name
import unittest
from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Carling", 5.00, 1.8)
        self.drink2 = Drink("Rosé", 7.50, 3.5)
        drink = [self.drink, self.drink2]

        self.pub = Pub("The Prancing Pony", 100.00, drink)
        self.pub1 = Pub("Bannermans", 200.00, drink)

       

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_has_cash(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_can_find_drink_by_name(self):
        drink = self.pub.find_drink_by_name("Carling")
        self.assertEqual("Carling", drink.name)

    def test_can_sell_drink_to_customer(self):
        customer = Customer("Stephen", 1000.00, 51)
        if customer.age >= 18 and customer.drunkenness < 9.0:
            self.pub.sell_drink_to_customer("Carling", customer)
            self.assertEqual(995.00, customer.wallet)
            self.assertEqual(105.00, self.pub.till)
            self.assertEqual(1, self.pub.drinks_sold)
            self.assertEqual(1.8, customer.drunkenness)
        else:
            print("Sorry mate, youre too young!")


    
    