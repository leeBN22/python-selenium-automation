#created by Leena on 05-June-2021 as part of HW3 Q0
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

@when('Search for {search_word}')
def search_for_product(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word, Keys.ENTER)

@when('Input Table in search field')
def search_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')

@when('Click on Amazon search icon')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

#added for HW3 Q4
@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    items_in_cart = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert items_in_cart == expected_count, f'Expected {expected_count}, but got {items_in_cart}'

#added by Leena on 12-June-2021 as per lesson 6 video for hamburger menu
# difference between find_element and find_elements is that the first will search for the exact element.
# If element not present, then error thrown. find_elements will also search but will not throw error
# instead it will give an empty list.

@then('Verify hamburger menu icon is visible')
def verify_ham_menu_visible(context):
    print('Using find_element')
    element = context.driver.find_element(By.ID, 'nav-hamburger-menu')
    print(element)
    print('Using find_elements ssss')
    elements = context.driver.find_elements(By.ID, 'nav-hamburger-menu')
    print(elements)

# added by Leena on 12-June-2021 as per lesson 6 video for find_elements example
@then('Verify {expected_count} footer links are displayed')
def verify_footer_links_amount(context, expected_count):
    link_count = len(context.driver.find_elements(By.CSS_SELECTOR,".navFooterDescItem a.nav_a"))
    assert link_count == int(expected_count), f'Expected 40 links, but got {link_count}'