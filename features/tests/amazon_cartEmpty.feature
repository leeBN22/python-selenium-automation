#created by Leena on 05-June-2021 as part of HW3 Q3
Feature: Shopping cart empty
  # Enter feature description here

  Scenario: To check if shopping cart is empty
    Given Open Amazon page
    #When Check cart icon number
    When Click on cart icon
    Then Verify shopping cart is empty