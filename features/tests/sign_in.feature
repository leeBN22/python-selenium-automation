#created by Leena on 05-June-2021 as part of HW3

Feature: Tests for sign in page

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened