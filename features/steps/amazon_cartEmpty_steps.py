#created by Leena on 05-June-2021 as part of HW3 Q3
from selenium.webdriver.common.by import By
from behave import given, when, then

# verify by clicking the cart icon and verifying if its empty
@when('Click on cart icon')
def open_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()

@then('Verify shopping cart is empty')
def verify_cart_empty(context):
    actual_result = context.driver.find_element(By.XPATH, "//h2[@class='sc-your-amazon-cart-is-empty']").text
    expected_result = 'Your Amazon Cart is empty'
    assert expected_result == actual_result, f'Expected result is {expected_result}, but got {actual_result}'

'''
# verifying by checking the cart icon number
@when('Check cart icon number')
def cart_number(context):
    cart_value = context.driver.find_element(By.ID, 'nav-cart-count').text
    print('Cart count is ' + cart_value)

@then('Verify shopping cart is empty')
def verify_cart_empty(context):
    actual_result = context.driver.find_element(By.ID, 'nav-cart-count').text
    expected_result = '0'
    assert expected_result == actual_result, f'Expected result is {expected_result}, but got {actual_result}'
'''