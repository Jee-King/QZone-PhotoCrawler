from selenium import webdriver

driver = webdriver.Firefox()

a = driver.get_cookies()
print(a)

b = {'name': 'weira', 'value': 'hahaha'}

driver.add_cookie(b)

print(driver.get_cookies())

driver.quit()