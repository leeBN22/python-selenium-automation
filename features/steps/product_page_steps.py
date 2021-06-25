#created by Leena on 12-June-2021 as part of HW3 Q4

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#Q4 added for HW4 Q2
@when('Click on Add to cart button')
def click_add_to_cart(context):
    # CLick on Add to Cart
    context.driver.find_element(By.ID, 'add-to-cart-button').click()

    # for shoes
    # if len(context.driver.find_element(By.ID, 'native_dropdown_selected_size_name')) == 1:
    #     #click  on Size dropdown
    #     context.driver.find_element(By.ID, 'native_dropdown_selected_size_name').click()
    #     #click on second size option
    #     context.driver.find_element(By.ID, 'size_name_2').click()
    #     sleep(3)
