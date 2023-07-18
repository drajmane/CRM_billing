import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Edge()
driver.maximize_window()

driver.get("https://seleniumbase.io/demo_page")

driver.find_element(By.ID,"myTextInput").click()

driver.current_url()


time.sleep(3)




