import unittest
from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Carling", 5.00, 1.8)
        self.drink2 = Drink("Rosé", 7.50, 3.5)
        drink = [self.drink, self.drink2]

        self.food = Food("Sausage Roll", 2.0, 1.0)
        self.food2 = Food("Pork Scratchings", 1.50, 0.6)
        self.food3 = Food("Bar Nuts", 0.10, 0.10)
        food = [self.food, self.food2, self.food3]

        self.stock = {
            self.drink: 75,
            self.drink2: 100
        }

        self.pub = Pub("The Prancing Pony", 100.00, drink, food)
        self.pub1 = Pub("Bannermans", 200.00, drink, food)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_pub_has_cash(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_can_find_drink_by_name(self):
        drink = self.pub.find_drink_by_name("Carling")
        self.assertEqual("Carling", drink.name)
    
    def test_can_find_food_by_name(self):
        food = self.pub.find_food_by_name("Sausage Roll")
        self.assertEqual("Sausage Roll", food.name)

    def test_can_sell_drink_to_customer(self):
        customer = Customer("Stephen", 1000.00, 51, 0)
        if customer.age >= 18 and customer.drunkenness < 9:
            self.pub.sell_drink_to_customer("Carling", customer)
            self.assertEqual(995.00, customer.wallet)
            self.assertEqual(105.00, self.pub.till)
            self.assertEqual(1, self.pub.drinks_sold)
            self.assertEqual(1.8, customer.drunkenness)
        else:
            print("Sorry mate, youre too young!")

    def test_food_changes_drunkenness_level(self):
        customer = Customer("Ricky", 20.0, 72, 10)
        self.pub.sell_food_to_customer("Sausage Roll", customer)
        self.assertEqual(9.0, customer.drunkenness)

    def test_total_value_of_stock(self):
        pub_val = self.pub.value_of_stock()
        self.assertEqual(1125, pub_val)