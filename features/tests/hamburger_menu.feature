#created by Leena on 12-June-2021 as per lesson 6 video
# difference between find_element and find_elements is that the first will search for the exact element.
Feature: Tests for Amazon Hamburger Menu

  Scenario: User sees Amazon Hamburger Menu icon
    Given Open Amazon page
    Then Verify hamburger menu icon is visible