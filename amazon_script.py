#created by Leena on 28-May-2021 as part of HW2
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#init driver
driver = webdriver.Chrome()
driver.maximize_window()

#open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')

driver.find_element(By.ID, 'nav-search-submit-button').click()

actual_result = driver.find_element(By.XPATH, "//span[@class = 'a-color-state a-text-bold']").text
print(f'Actual result :{actual_result}')

expected_result = '"Table"'
assert expected_result.lower() == actual_result.lower(), f'Expected result is {expected_result}, but got {actual_result}'

driver.quit()
