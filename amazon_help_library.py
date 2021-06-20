#created by Leena on 28-May-2021 as part of HW2 Q2
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.amazon.com/gp/help/customer/display.html')


search = driver.find_element(By.ID, 'helpsearch')
search.clear()
search.send_keys('Cancel order')
search.send_keys(Keys.RETURN)

#actual_result = driver.find_element(By.XPATH, "//div[@class = 'a-box a-spacing-extra-large a-color--background answer-box answer-box-t1']//div[@class ='a-box-inner']//div[@class='help-content']//a[@name='GUID-159D403A-3B08-477C-88E3-58C737822D49']/../h1").text
# added below as part of comments from Lana
actual_result = driver.find_element(By.XPATH, "//div[@class='help-content']//h1").text
print(f'Actual result : {actual_result}')

expected_result = 'Cancel Items or Orders'
assert expected_result.lower() == actual_result.lower(), f'Expected result is {expected_result}, but got {actual_result}'

driver.quit()