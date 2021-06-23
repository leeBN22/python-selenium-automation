#created by Leena on 12-June-2021 as per lesson 6 video for HW3 Q3,Q4
from selenium.webdriver.common.by import By
from behave import given, when, then

@then('"{expected_text}" message is displayed')
def verify_empty_cart_msg(context, expected_text):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '#sc-active-cart h2').text
    assert actual_text == expected_text, f'Expected {expected_text}, but got {actual_text}'