from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_in_test2():
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()

    driver.set_window_position(0, -1600)
    driver.maximize_window()
    url = "https://test.mensa.no/"
    driver.get(url)

    xpath_18_50 = "//*[@class=\"age button btn btn-success ageselect_1850\"]"
    (WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath_18_50)))).click()

    xpath_start = "//*[@id=\"startTest\"]"
    (WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath_start)))).click()
    x = 0
    time.sleep(1)  # без цього тайм сліпу не хоче працювати(
    while x < 38:
        try:
            print("Click" + str(x))
            xPath_el = "(//*[@id=\"question_" + str(x) + "\"]//div[@data-answerid=\"2\"])"
            print(xPath_el)
            el = WebDriverWait(driver, 1000).until(
                EC.presence_of_element_located(
                    ((By.XPATH, xPath_el))))

            el.click()
            x = x + 1
            time.sleep(1)
        except:
            if x == 35:
                print("We had" + str(x) + "questions")
                break
            else:
                print("Something went wrong")
                break
