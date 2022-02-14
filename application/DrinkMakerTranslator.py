class DrinkMakerTranslator(object):

    @staticmethod
    def translate(instruction):
        drink = instruction.drink
        price = drink.price
        quantity = instruction.quantity
        money = instruction.money
        if money < price * quantity:
            missing_money = int(price * quantity - money)
            return f'M:{missing_money}'
        sugar = f'{instruction.sugar}' if instruction.sugar > 0 else ""
        sticks = "0" if instruction.sugar > 0 else ""
        return f'{drink.name}:{sugar}:{sticks}'
