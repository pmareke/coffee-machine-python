class Instruction(object):
    def __init__(self, drink, quantity, sugar, money):
        if quantity < 0:
            raise NameError("Invalid quantity")
        if sugar < 0:
            raise NameError("Invalid sugar")
        if money < 0:
            raise NameError("Invalid money")
        self.drink = drink
        self.quantity = quantity
        self.sugar = sugar
        self.money = money
