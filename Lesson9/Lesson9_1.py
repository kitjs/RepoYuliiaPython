import time
from selenium import webdriver

driver=webdriver.Chrome() #об'єкт класу веб драйвер
#url="https://www.selenium.dev"
#driver.get(url)

driver.maximize_window()
sites=["https://www.ispanskamova.com","https://talkpal.ai/"]
for url in sites:
    driver.get(url)
    driver.get_screenshot_as_file(f"screenshots/{url[url.find("/")+2:url.rfind(".")]}.png")
    time.sleep(1)