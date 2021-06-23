#created by Leena on 12-June-2021 as per lesson 6 video for HW3 Q3,Q4

#Q3
Feature: Test Amazon Cart

  Scenario: User sees empty shopping cart
    Given Open Amazon page
    When Click on cart icon
    Then "Your Amazon Cart is empty" message is displayed

#Q4
Scenario: User can add a product to the cart
  Given Open Amazon page
  When Search for coffee mug
  And Click on the first product
  And Click on Add to cart button
  Then Verify cart has 1 item

  """
Scenario: User can add a product to the cart
  Given Open Amazon page
  When Search for shoes
  And Click on the first product
  And Click on Add to cart button
  Then Verify cart has 1 item
"""
