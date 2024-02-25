from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.implicitly_wait(5)


def start_win_2():
    driver.set_window_position(0,-1600)
    driver.maximize_window()
    url="https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html"
    driver.get(url)
    time.sleep(1)


def fill_in_fields_2():
    driver.implicitly_wait(10)
    x=1
    while x<36:
        if 0<x<9:
            input_field_xpath="//input[@name=\"q"+str(x)+"\"]"
            input_field=driver.find_element(By.XPATH, input_field_xpath )
            input_field.click()
            input_field.clear()
            input_field.send_keys("5")
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

start_win_2()
fill_in_fields_2()


