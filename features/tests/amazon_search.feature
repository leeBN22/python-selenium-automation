#created by Leena on 05-June-2021 as part of HW3
Feature: Test Amazon search

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Table in search field
    And Click on Amazon search icon
    Then Verify search worked