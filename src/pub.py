class Pub:
    def __init__(self, _name, _till, _drink, _food):
        self.name = _name
        self.till = _till
        self.drink = _drink
        self.food = _food
        self.drinks_sold = 0
        self.stock = {}
        

    def increase_till(self, amount):
        self.till += amount

    def increase_drinks_sold(self):
        self.drinks_sold += 1
    
    def find_drink_by_name(self, drink_name):
        for drink in self.drink:
            if drink.name == drink_name:
                return drink
    
    def find_food_by_name(self, food_name):
        for food in self.food:
            if food.name == food_name:
                return food
    
    def sell_drink_to_customer(self, name, customer):
        if customer.age >= 18 and customer.drunkenness > 9.0:
            return
        else:
            drink = self.find_drink_by_name(name)
            customer.reduce_wallet(drink.price)
            self.increase_drinks_sold()
            customer.increase_drunkenness(drink.alcohol_level)
            self.increase_till(drink.price)
        

    def sell_food_to_customer(self, name, customer):
        food = self.find_food_by_name(name)
        customer.decrease_drunkenness(food.rejuvination_level)

    def value_of_stock(self):
        total_value = 0
        for stock in self.stock:
            total_value += (2 * stock)
        return total_value



