#created by Leena on 05-June-2021 as part of HW3 Q2
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('Open Amazon Help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Input Cancel order in Search Help Library field')
def search_amazon_help(context):
    search = context.driver.find_element(By.ID, 'helpsearch')
    search.clear()
    search.send_keys('Cancel order')

@when('Hit enter key')
def click_enter(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys(Keys.RETURN)

@then('Verify that ‘Cancel Items or Orders’ text is present')
def verify_result(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='help-content']//h1").text
    print(f'Actual result : {actual_result}')
    expected_result = 'Cancel Items or Orders'
    assert expected_result.lower() == actual_result.lower(), f'Expected result is {expected_result}, but got {actual_result}'
