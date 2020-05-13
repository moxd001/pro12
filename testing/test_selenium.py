from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
sleep(2)
driver.quit()