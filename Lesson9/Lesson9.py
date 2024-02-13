import time
from selenium import webdriver

driver=webdriver.Chrome() #об'єкт класу веб драйвер
driver.get("https://www.selenium.dev")
driver.maximize_window()
driver.get_screenshot_as_file("screenshots/selenium.png")
time.sleep(50)