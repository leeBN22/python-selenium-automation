#created by Leena on 05-June-2021 as part of HW3
Feature: Test Amazon search

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Table in search field
    And Click on Amazon search icon
    Then Verify search worked

# added by Leena on 12-June-2021 as per lesson 6 video for find_elements example
  Scenario: Amazon footer has correct amount of links
    Given Open Amazon page
    Then Verify 40 footer links are displayed