Feature: DrinkMakerTranslator

  Scenario: with enough money
    Scenario: The drink maker should receive the correct instruction for my tea
      Given we want a Tea with sugar
      Given we create an instruction with sugar
      When we send the instruction to the translator
      Then the order is made with a stick
    Scenario: The drink maker should receive the correct instruction for my hot coffee
      Given we want a hot Coffee
      Given we create an instruction without sugar
      When we send the instruction to the translator
      Then the order is made without a stick
  Scenario: with not enough money
    Scenario: The drink maker should send a message
      Given we want an Orange Juice
      Given we create an instruction without enough money
      When we send the instruction to the translator
      Then the order is not made
