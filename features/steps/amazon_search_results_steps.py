#created by Leena on 05-June-2021 as part of HW3 Q0,Q4
from selenium.webdriver.common.by import By
from behave import given, when, then

#Q4 added for HW4 Q2
@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(By.XPATH,"//div[@data-component-type='s-search-result']//a[.//span[@class = 'a-price']]").click()
    #context.driver.find_element(By.XPATH,"//div[@class = 'a-row a-size-base a-color-base']//a[@class = 'a-size-base a-link-normal a-text-normal']//span[@class= 'a-price']//span[@class ='a-offscreen']").click()


#Q0
@then('Verify search worked')
def verify_search_worked(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class = 'a-color-state a-text-bold']").text
    print(f'Actual result :{actual_result}')
    expected_result = '"Table"'
    assert expected_result.lower() == actual_result.lower(), f'Expected result is {expected_result}, but got {actual_result}'