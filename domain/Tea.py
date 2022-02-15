from domain.Drink import Drink


class Tea(Drink):
    def __init__(self, type="normal"):
        name = "Tc" if type == 'hot' else "T"
        super(Tea, self).__init__(name, 0.4)
