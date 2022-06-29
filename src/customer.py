class Customer:
    def __init__(self, _name, _wallet, _age):
        self.name = _name
        self.wallet = _wallet
        self.age = _age
        self.drunkenness = 0
    
    def reduce_wallet(self, amount):
        self.wallet -= amount
    
    
    def increase_drunkenness(self, amount):
        self.drunkenness += amount