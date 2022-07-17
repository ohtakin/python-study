import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import Keys
from selenium.webdriver.common.by import By

# browser = webdriver.Chrome(
#     "/Users/takinoh/Documents/GitHub/python-study/chromedriver")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://naver.com")

# elem = browser.find_element_by_class_name("link_login")
elem = browser.find_element(By.CLASS_NAME, "link_login")
# print(elem)
elem.click()

browser.find_element(By.ID, "id").send_keys("naverId")
browser.find_element(By.ID, "pw").send_keys("naverPassword")

time.sleep(3)
browser.find_element(By.ID, "log.login").click()

browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("testNaver")

print(browser.page_source)

time.sleep(3)
browser.close()
