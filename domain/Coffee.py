from domain.Drink import Drink


class Coffee(Drink):
    def __init__(self, type="normal"):
        name = "Ch" if type == 'hot' else "C"
        super(Coffee, self).__init__(name, 0.6)
