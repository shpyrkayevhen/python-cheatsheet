# Using Selenium
# 1: pip install selenium
# 2: Installing drivers for Chrome/FireFox/... from pypi.org
# 3: Add this drivers to Path local computer


# webdriver module has a different classes represents all browsers
# These classes return -> Browser Object
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://github.com')

# Inspect elemens which we wants to click and find their (id|class|nme|tag)

# We can also can find some element for a text -> return web element
signin_link = browser.find_element(By.LINK_TEXT, "Sign in")
signin_link.click()


browser.get('https://github.com/login')
# Fill in login field
username_input = browser.find_element(By.NAME, "login")
username_input.send_keys("shpyrkayevhen@gmail.com")

# Fill in login field
password_input = browser.find_element(By.NAME, "password")
password_input.send_keys("nesik199610")
password_input.submit()


# browser.find_element(By.CLASS_NAME, '')

# Return html conent of this page

# Перевіряємо, автоматично тестуємо чи є такий елемент з назвою на сторінці
# assert 'shpyrkayevhen' in browser.page_source
