class DrinkMakerTranslator(object):

    @staticmethod
    def translate(instruction):
        drink = instruction.drink
        sugar = f'{instruction.sugar}' if instruction.sugar > 0 else ""
        sticks = "0" if instruction.sugar > 0 else ""
        return f'{drink.name}:{sugar}:{sticks}'
