#created by Leena on 05-June-2021 as part of HW3 Q0
from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@when('Input Table in search field')
def search_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')

@when('Click on Amazon search icon')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

