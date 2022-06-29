class Pub:
    def __init__(self, _name, _till, _drink):
        self.name = _name
        self.till = _till
        self.drink = _drink
        self.drinks_sold = 0

    def increase_till(self, amount):
        self.till += amount

    def increase_drinks_sold(self):
        self.drinks_sold += 1
    
    def find_drink_by_name(self, drink_name):
        for drink in self.drink:
            if drink.name == drink_name:
                return drink
    
    def sell_drink_to_customer(self, name, customer):
        drink = self.find_drink_by_name(name)
        customer.reduce_wallet(drink.price)
        self.increase_drinks_sold()
        customer.increase_drunkenness(drink.alcohol_level)
        self.increase_till(drink.price)
