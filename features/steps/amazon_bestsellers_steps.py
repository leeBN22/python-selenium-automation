#created by Leena on 14-June-2021 as per HW4 Q1

from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon Best Sellers page')
def open_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify {link_count} links are present at the top')
def link_bestsellers_count(context, link_count):
    links = context.driver.find_elements(By.CSS_SELECTOR, "a[href *= 'ref=zg_bs_tab']")
    #or (By.CSS_SELECTOR, '#zg_tabs a')
    assert len(links) == int(link_count),f'Expected {link_count} but got {len(links)}'
