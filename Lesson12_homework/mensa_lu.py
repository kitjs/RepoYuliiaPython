
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()


def start_win():
    driver.set_window_position(0,-1600)
    driver.maximize_window()
    url="https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html"
    driver.get(url)
    time.sleep(1)


def fill_in_fields():
    x=1
    while x<36:
        if 0<x<9:
            input_field_xpath="//input[@name=\"q"+str(x)+"\"]"
            input_field_wait=(WebDriverWait(driver, 30).until(
                 EC.presence_of_element_located(By.XPATH, input_field_xpath )))
            input_field_wait.click()
            input_field_wait.clear()
            input_field_wait.send_keys("5")
            x=x+1
            print(x)
        elif 8<x<19:
            driver.find_element("xpath", "//input[@name=\"q"+str(x)+"\" and @value=\"c\"]").click()
            x = x + 1
            print(x)
        elif 18<x<23:
            driver.find_element("xpath", "//input[@name=\"q"+str(x)+"\" and @value=\"c\"]").click()
            driver.find_element("xpath", "//input[@name=\"q"+str(x)+"\" and @value=\"d\"]").click()
            x = x + 1
            print(x)
        elif 22<x<27:
            driver.find_element("xpath", "//input[@name=\"q"+str(x)+"\" and @value=\"c\"]").click()
            x = x + 1
            print(x)
        elif 26<x<34:
            driver.find_element("xpath", "//input[@name=\"q"+str(x)+"\" and @value=\"d\"]").click()
            x = x + 1
            print(x)
        else:
            break



