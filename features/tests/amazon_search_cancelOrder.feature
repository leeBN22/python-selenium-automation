#created by Leena on 05-June-2021 as part of HW3 Q2
Feature: Search for Cancelling an order on Amazon

  Scenario: User can search for solutions of Cancelling an order on Amazon
    Given Open Amazon Help page
    When Input Cancel order in Search Help Library field
    And Hit enter key
    Then Verify that ‘Cancel Items or Orders’ text is present