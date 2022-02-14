class Instruction(object):
    def __init__(self, drink, quantity, sugar):
        if quantity < 0:
            raise NameError("Invalid quantity")
        if sugar < 0:
            raise NameError("Invalid sugar")
        self.drink = drink
        self.quantity = quantity
        self.sugar = sugar
