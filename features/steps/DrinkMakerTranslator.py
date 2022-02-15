from behave import *
from application.DrinkMakerTranslator import DrinkMakerTranslator
from domain.Coffee import Coffee
from domain.Instruction import Instruction
from domain.OrangeJuice import OrangeJuice

from domain.Tea import Tea


@given('we want a Tea with sugar')
def step_impl(context):
    context.drink = Tea()


@given('we want a hot Coffee')
def step_impl(context):
    context.drink = Coffee("hot")


@given('we want an Orange Juice')
def step_impl(context):
    context.drink = OrangeJuice()


@given('we create an instruction with sugar')
def step_impl(context):
    context.instruction = Instruction(context.drink, 1, 1, 1)


@given('we create an instruction without sugar')
def step_impl(context):
    context.instruction = Instruction(context.drink, 1, 0, 1)


@given('we create an instruction without enough money')
def step_impl(context):
    context.instruction = Instruction(context.drink, 10, 1, 1)


@when('we send the instruction to the translator')
def step_impl(context):
    context.message = DrinkMakerTranslator.translate(context.instruction)


@then('the order is made with a stick')
def step_impl(context):
    assert context.message == "T:1:0"


@then('the order is made without a stick')
def step_impl(context):
    assert context.message == "Ch::"


@then('the order is not made')
def step_impl(context):
    assert context.message == "M:5"
