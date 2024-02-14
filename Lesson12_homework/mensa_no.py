def fill_in_test2():
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()

    driver.set_window_position(0, -1600)
    driver.maximize_window()
    url = "https://test.mensa.no/"
    driver.get(url)

    xpath_18_50 = "//*[@class=\"age button btn btn-success ageselect_1850\"]"
    time.sleep(1)
    driver.find_element("xpath", xpath_18_50).click()
    xpath_start = "//*[@id=\"startTest\"]"
    time.sleep(1)
    driver.find_element("xpath", xpath_start).click()
    time.sleep(1)
    x = 0
    while x < 38:
        try:
            driver.find_element("xpath", "(//*[@id=\"question_" + str(x) + "\"]//div[@data-answerid=\"2\"])").click()
            print("Click" + str(x))
            x = x + 1
            time.sleep(1)
        except:
            if x == 35:
                print("We had" + str(x) + "questions")
                break
            else:
                print("Something went wrong")
                break
