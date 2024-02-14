from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xpathDumskaya as x
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.set_window_position(0,1850)
driver.maximize_window()

driver.get("https://dumskaya.net")


enter_button = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "myDynamicElement")))
enter_button.click()
time.sleep(3)

registration_button = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located ((By.XPATH, x.registration_button)))
registration_button.click()
time.sleep(5)

email_field =  WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, x.email_field)))
email_field.send_keys(user_data.email)
time.sleep(3)

nick_field =  WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, x.nick_field)))
nick_field.send_keys(user_data.nick)
time.sleep(3)

password_field = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, x.password_field)))
password_field.send_keys(user_data.password)
time.sleep(3)

password2_field =  WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, x.password2_field)))
password2_field.send_keys(user_data.password)
time.sleep(3)

male_radio =  WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, x.male_radio)))
male_radio.click()
time.sleep(3)

finish_button = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, x.finish_button)))
finish_button.click()

time.sleep(5)
time.sleep(300)