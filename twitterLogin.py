import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# firefox_options = Options()
# firefox_options.headless = True
os.environ["PATH"] += r"C:\FireFoxSelenium"
driver = webdriver.Firefox()
# driver = webdriver.Firefox(options=firefox_options)
driver.get("https://twitter.com")

homeLoginBtn  = driver.find_element(By.XPATH,"//a[contains(@href,'/login')]")
homeLoginBtn.click()
time.sleep(4)
#For Entering UserName
userNameInput = driver.find_element(By.XPATH,"//input[contains(@autocomplete,'username')]")
userNameInput.send_keys("ArunSha365161")
nextButton = driver.find_element(By.XPATH,"//div[contains(@role,'button')][2]/div/span/span")
nextButton.click()
#For Entering UserPassword
time.sleep(4)
userPasswordInput = driver.find_element(By.XPATH,"//input[contains(@autocomplete,'current-password')]")
userPasswordInput.send_keys("SHa.arun*99#")
nextButton = driver.find_element(By.XPATH,"//div[contains(@role,'button')]/div/span/span")
nextButton.click()


driver.quit() 
# //a[contains(@href,"/explore")]