from mamba import description, it
from expects import expect, equal

from application.DrinkMakerTranslator import DrinkMakerTranslator
from domain.Chocolate import Chocolate
from domain.Coffee import Coffee
from domain.Instruction import Instruction
from domain.Tea import Tea

with description('DrinkMakerTranslator') as self:
    with it('The drink maker should receive the correct instruction for my tea'):
        instruction = Instruction(Tea(), 1, 1)
        expect(DrinkMakerTranslator.translate(instruction)).to(equal("T:1:0"))

    with it('I want to be able to send instruction to the drink maker to add one or two sugars'):
        instruction = Instruction(Chocolate(), 0, 0)
        expect(DrinkMakerTranslator.translate(instruction)).to(equal("H::"))

    with it('When my order contains sugar the drink maker should add a stick with it'):
        instruction = Instruction(Coffee(), 1, 2)
        expect(DrinkMakerTranslator.translate(instruction)).to(equal("C:2:0"))
