from mamba import description, it
from expects import expect, equal

from application.DrinkMakerTranslator import DrinkMakerTranslator
from domain.Chocolate import Chocolate
from domain.Coffee import Coffee
from domain.Instruction import Instruction
from domain.OrangeJuice import OrangeJuice
from domain.Tea import Tea

with description('DrinkMakerTranslator') as self:
    with description('with enough money') as self:
        with it('The drink maker should receive the correct instruction for my tea'):
            instruction = Instruction(Tea(), 1, 1, 1)
            expect(DrinkMakerTranslator.translate(
                instruction)).to(equal("T:1:0"))

            with it('I want to be able to send instruction to the drink maker to add one or two sugars'):
                instruction = Instruction(Chocolate(), 0, 0, 1)
                expect(DrinkMakerTranslator.translate(
                    instruction)).to(equal("H::"))
            with it('When my order contains sugar the drink maker should add a stick with it'):
                instruction = Instruction(OrangeJuice(), 1, 2, 1)
                expect(DrinkMakerTranslator.translate(
                    instruction)).to(equal("O:2:0"))
            with it('I want to order hot  coffee'):
                instruction = Instruction(Coffee('hot'), 1, 2, 1)
                expect(DrinkMakerTranslator.translate(
                    instruction)).to(equal("Ch:2:0"))
    with description('with not enough money') as self:
        with it('should sends a message to the drink maker'):
            instruction = Instruction(Tea(), 10, 1, 1)
            expect(DrinkMakerTranslator.translate(
                instruction)).to(equal("M:3"))
