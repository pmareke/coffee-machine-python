from domain.Drink import Drink


class OrangeJuice(Drink):
    def __init__(self):
        super(OrangeJuice, self).__init__("O", 0.6)
