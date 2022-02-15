from domain.Drink import Drink


class Chocolate(Drink):
    def __init__(self, type="normal"):
        name = "Hc" if type == 'hot' else "H"
        super(Chocolate, self).__init__(name, 0.5)
