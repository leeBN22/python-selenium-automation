#created by Leena on 05-June-2021 as part of HW3 Q0,Q4
from selenium.webdriver.common.by import By
from behave import given, when, then

#Q4

@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(By.XPATH,'').click() #doubt


#Q0
@then('Verify search worked')
def verify_search_worked(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class = 'a-color-state a-text-bold']").text
    print(f'Actual result :{actual_result}')
    expected_result = '"Table"'
    assert expected_result.lower() == actual_result.lower(), f'Expected result is {expected_result}, but got {actual_result}'

