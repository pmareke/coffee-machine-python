from mamba import description, it
from expects import expect, equal, raise_error

from application.DrinkMakerTranslator import DrinkMakerTranslator
from domain.Chocolate import Chocolate
from domain.Instruction import Instruction
from domain.Tea import Tea


with description('Instruction') as self:
    with it('should creates an instruction'):
        instruction = Instruction(Tea(), 1, 1)
        expect(instruction.drink.name).to(equal("T"))

    with it('should raises an exception creating an instruction'):
        expect(lambda:  Instruction(Chocolate(), -1, 1)
               ).to(raise_error(NameError))
        expect(lambda:  Instruction(Chocolate(), 1, -1)
               ).to(raise_error(NameError))
