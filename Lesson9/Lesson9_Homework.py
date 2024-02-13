# Домашня робота
# Створити новий проект та додати до нього Selenium.
# Написати автоматизацію яка заходить на 10 сайтів,
# та натискає на мінімум 3 кнопки меню,
# в кожному з них.
# По аналогії з Lesson_9_3


#можна запускати у такому вигляді як є

import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException, ElementNotInteractableException

driver = webdriver.Chrome()
driver.maximize_window()

sites = ["https://www.w3schools.com/python/python_try_except.asp", "https://www.browserstack.com/",
         "https://lingualeo.com/en","https://djinni.co/login","https://training.epam.com/en",
         "https://taxer.ua/ru/","https://www.infojobs.net/","https://www.py4e.com/",
         "https://acode.com.ua/","https://klopotenko.com/snidanki/" ]

#SITE_1
driver.get(sites[0])
url1=sites[0]
try:
    #Accept cookies
    accept_choice = driver.find_element("xpath","//*[@id=\"accept-choices\"]")
    accept_choice.click()
    #Click on first button
    site1_button1 = driver.find_element("xpath","//*[@id=\"subtopnav\"]/a[@title=\"CSS Tutorial\"]")
    site1_button1.click()
    driver.get_screenshot_as_file(f"screenshots/{url1[url1.find("/") + 2:url1.rfind(".")]}1.png")
    #Click on second button
    site1_button2 = driver.find_element("xpath", "//*[@id=\"subtopnav\"]/a[@title=\"JavaScript Tutorial\"]")
    site1_button2.click()
    driver.get_screenshot_as_file(f"screenshots/{url1[url1.find("/") + 2:url1.rfind(".")]}2.png")
    #Click on third button
    site1_xpath_button3 = driver.find_element("xpath", "//*[@id=\"subtopnav\"]/a[@title=\"PHP Tutorial\"]")
    site1_xpath_button3.click()
    driver.get_screenshot_as_file(f"screenshots/{url1[url1.find("/") + 2:url1.rfind(".")]}3.png")

    # SITE_2
    driver.get(sites[1])
    url2 = sites[1]
    time.sleep(5)

    # Do 1st click
    site2_button1 = driver.find_element("xpath","//*[@id=\"developers-new-dd-toggle\"]")
    try:
        site2_button1.click()
    except ElementNotInteractableException:
        driver.refresh()
        site2_button1.click()
    time.sleep(2)

    #open hidden menu and click on item
    site2_button1_1 = driver.find_element("xpath","//*[@id=\"developers-new-dd-menu\"]//a[@title=\"Security\"]")
    site2_button1_1.click()
    time.sleep(2)
    driver.get_screenshot_as_file(f"screenshots/{url2[url2.find("/") + 2:url2.rfind(".")]}1.png")

    # Do 2nd click
    site2_button2 = driver.find_element("xpath", "//a[@title=\"Pricing\"]")
    site2_button2.click()
    driver.get_screenshot_as_file(f"screenshots/{url2[url2.find("/") + 2:url2.rfind(".")]}2.png")

    # Do 3rd click
    site2_button3 = driver.find_element("xpath", "//*[@id=\"doc-menu-toggle\"]")
    site2_button3.click()
    driver.get_screenshot_as_file(f"screenshots/{url2[url2.find("/") + 2:url2.rfind(".")]}3.png")
except:
    print("Something wrong in 1st")

# SITE_3
driver.get(sites[2])
url3 = sites[2]
time.sleep(5)

try:
    # Do 1st click
    site3_button1 = driver.find_element("xpath","//*[@class=\"ll-leokit__site-menu-top-item__content__title\"]")
    site3_button1.click()
    time.sleep(5)
    driver.get_screenshot_as_file(f"screenshots/{url3[url3.find("/") + 2:url3.rfind(".")]}1.png")

    # Do 2nd click
    #не можу клік зробити на цю кнопку. Як ії мені знайти?
    # site3_button2 = driver.find_element("xpath", "//*[@id=\"topitem-jungle-video\"]")
    # try:
    #     site3_button2.click()
    # except ElementNotInteractableException:
    #     driver.refresh()
    #     time.sleep(10)
    #     type(site3_button2)
    #     site3_button2.click()

    site3_button2 = driver.find_element("xpath", "//*[@class=\"ll-premium-indicator__text\"]")
    site3_button2.click()
    time.sleep(2)
    driver.get_screenshot_as_file(f"screenshots/{url3[url3.find("/") + 2:url3.rfind(".")]}2.png")

    # Do 3rd click
    site2_button3 = driver.find_element("xpath", "//*[@class=\"ll-leokit__button__content\"]")
    site2_button3.click()
    driver.get_screenshot_as_file(f"screenshots/{url3[url3.find("/") + 2:url3.rfind(".")]}3.png")
except:
    print("Something wrong in 2")

# SITE_4
driver.get(sites[3])
url4 = sites[3]
time.sleep(5)

try:
    # Do 1st click
    driver.find_element("xpath",
                                              "//*[contains(text(), \"Privacy\")]").click()
    time.sleep(4)
    driver.get_screenshot_as_file(f"screenshots/{url4[url4.find("/") + 2:url4.rfind(".")]}1.png")
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(4)

    # Do 2nd click
    driver.find_element("xpath", "//*[contains(text(), \"Suggest an idea\")]").click()
    time.sleep(4)
    driver.get_screenshot_as_file(f"screenshots/{url4[url4.find("/") + 2:url4.rfind(".")]}2.png")
    driver.switch_to.window(driver.window_handles[0])

    #Do 3rd click
    driver.find_element("xpath", "//*[contains(text(), \"Blog\")]").click()
    driver.get_screenshot_as_file(f"screenshots/{url4[url4.find("/") + 2:url4.rfind(".")]}3.png")
except:
    print("Something wrong in 3")

# SITE_5
driver.get(sites[5])
url5 = sites[5]
time.sleep(5)
try:
    # Do 1st click
    driver.find_element("xpath","//*[contains(text(), \" Календарь \")]").click()
    time.sleep(4)
    driver.get_screenshot_as_file(f"screenshots/{url5[url5.find("/") + 2:url5.rfind(".")]}1.png")

    # Do 2nd click
    driver.find_element("xpath", "//*[contains(text(), \" Бланки \")]").click()
    time.sleep(4)
    driver.get_screenshot_as_file(f"screenshots/{url5[url5.find("/") + 2:url5.rfind(".")]}2.png")

    #Do 3rd click
    driver.find_element("xpath", "//*[contains(text(), \" Блог \")]").click()
    driver.get_screenshot_as_file(f"screenshots/{url5[url5.find("/") + 2:url5.rfind(".")]}3.png")
except:
    print("Something wrong in 5")


#SITE_6 capcha
driver.get(sites[6])
url6 = sites[6]
time.sleep(5)
#Accept cookies
try:
    driver.find_element("xpath","//*[@id=\"didomi-notice-agree-button\"]").click()
    time.sleep(4)

    # Do 1st click
    driver.find_element("xpath","//*[@id=\"menu_tab_25\")]").click()
    time.sleep(4)
    driver.get_screenshot_as_file(f"screenshots/{url6[url6.find("/") + 2:url6.rfind(".")]}1.png")

    # Do 2nd click
    driver.find_element("xpath", "//*[@id=\"menu_tab_33\")]").click()
    time.sleep(4)
    driver.get_screenshot_as_file(f"screenshots/{url6[url6.find("/") + 2:url6.rfind(".")]}2.png")

    #Do 3rd click
    driver.find_element("xpath", "//*[@id=\"menu_tab_34\")]").click()
    driver.get_screenshot_as_file(f"screenshots/{url6[url6.find("/") + 2:url6.rfind(".")]}3.png")
except:
    print("Here is capcha or something is wrong in 6")


# SITE_7
driver.get(sites[7])
url7 = sites[7]
time.sleep(5)
try:
    # Do 1st click
    driver.find_element("xpath","//*[contains(text(), \"Lesson\")]").click()
    time.sleep(4)
    driver.get_screenshot_as_file(f"screenshots/{url7[url7.find("/") + 2:url7.rfind(".")]}1.png")

    # Do 2nd click
    driver.find_element("xpath", "//*[contains(text(), \"Discussions\")]").click()
    time.sleep(4)
    driver.get_screenshot_as_file(f"screenshots/{url7[url7.find("/") + 2:url7.rfind(".")]}2.png")

    #Do 3rd click
    driver.find_element("xpath", "//*[contains(text(), \"OER\")]").click()
    driver.get_screenshot_as_file(f"screenshots/{url7[url7.find("/") + 2:url7.rfind(".")]}3.png")
except:
    print("Something wrong in 7")

# SITE_8
driver.get(sites[8])
url8 = sites[8]
time.sleep(5)
try:
    # Do 1st click
    driver.find_element("xpath","//*[contains(text(), \"C++\")]").click()
    time.sleep(4)
    driver.get_screenshot_as_file(f"screenshots/{url8[url8.find("/") + 2:url8.rfind(".")]}1.png")

    # Do 2nd click
    driver.find_element("xpath", "//*[contains(text(), \"Linux\")]").click()
    time.sleep(4)
    driver.get_screenshot_as_file(f"screenshots/{url8[url8.find("/") + 2:url8.rfind(".")]}2.png")

    #Do 3rd click
    driver.find_element("xpath", "//*[contains(text(), \"SQL\")]").click()
    driver.get_screenshot_as_file(f"screenshots/{url8[url8.find("/") + 2:url8.rfind(".")]}3.png")
except:
    print("Something wrong in 8")

# SITE_9
driver.get(sites[9])
url9 = sites[9]
time.sleep(5)
try:
    #Accept cookies
    driver.find_element("xpath","//*[@class=\"fc-footer-buttons\"]/button/p").click()
    time.sleep(4)
    # Do 1st click
    driver.find_element("xpath","//*[@id=\"site-navigation\"]//li[2]").click()
    time.sleep(4)
    driver.get_screenshot_as_file(f"screenshots/{url9[url9.find("/") + 2:url9.rfind(".")]}1.png")

    # Do 2nd click
    driver.find_element("xpath", "//*[@id=\"site-navigation\"]//li[1]").click()
    time.sleep(4)
    driver.get_screenshot_as_file(f"screenshots/{url9[url9.find("/") + 2:url9.rfind(".")]}2.png")

    #Do 3rd click
    driver.find_element("xpath", "//*[@id=\"site-navigation\"]//li[3]").click()
    driver.get_screenshot_as_file(f"screenshots/{url9[url9.find("/") + 2:url9.rfind(".")]}3.png")
except:
    print("Something wrong in 9")

# SITE_10
driver.get(sites[4])
url = sites[4]
time.sleep(5)
try:
    # Do 1st click
    driver.find_element("xpath","//*[contains(text(), \"Programs\")]").click()
    time.sleep(4)
    driver.get_screenshot_as_file(f"screenshots/{url[url.find("/") + 2:url.rfind(".")]}1.png")

    # Do 2nd click
    driver.find_element("xpath", "//*[contains(text(), \"Skills\")]").click()
    time.sleep(4)
    driver.get_screenshot_as_file(f"screenshots/{url[url.find("/") + 2:url.rfind(".")]}2.png")

    #Do 3rd click
    driver.find_element("xpath", "//*[contains(text(), \"Blog\")]").click()
    driver.get_screenshot_as_file(f"screenshots/{url[url.find("/") + 2:url.rfind(".")]}3.png")
except:
    print("Something wrong in 10")
driver.close()
