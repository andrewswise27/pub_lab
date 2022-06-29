import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Ricky", 20.00)
        self.customer2 = Customer("Stephen", 1000.00)
    
    def test_customer_has_name(self):
        self.assertEqual("Ricky", self.customer.name)

    def test_customer_has_cash(self):
        self.assertEqual(1000.00, self.customer2.wallet)