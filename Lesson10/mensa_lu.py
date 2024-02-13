from selenium import webdriver
import time

driver=webdriver.Chrome()

driver.set_window_position(0,-1600)
driver.maximize_window()
url="https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html"
driver.get(url)
time.sleep(1)
x=1
while x<36:
    if 0<x<9:
        driver.find_element("xpath", "//input[@name=\"q"+str(x)+"\"]").click()
        driver.find_element("xpath", "//input[@name=\"q"+str(x)+"\"]").clear()
        driver.find_element("xpath", "//input[@name=\"q"+str(x)+"\"]").send_keys("5")
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



