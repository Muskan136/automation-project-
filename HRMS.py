import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

path = "E:\\geckodriver.exe"
s = Service(executable_path=path)
driver = webdriver.Firefox(service=s)

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(1)
driver.find_element(By.XPATH,"//button[@type='submit']",).click()
time.sleep(1)
driver.find_element(By.XPATH,"//span[text()='Admin']").click()
time.sleep(1)
#automation
#qe and qa
#connecting to the github
