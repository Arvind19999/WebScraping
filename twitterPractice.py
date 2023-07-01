import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

os.environ["PATH"] += r"C:\FireFoxSelenium"
driver = webdriver.Firefox()
driver.get("https://twitter.com")

homeLoginBtn = driver.find_element(By.XPATH, "//a[contains(@href,'/login')]")
homeLoginBtn.click()
time.sleep(4)

userNameInput = driver.find_element(By.XPATH, "//input[contains(@autocomplete,'username')]")
userNameInput.send_keys("ArunSha365161")

nextButton = driver.find_element(By.XPATH, "//div[contains(@role,'button')][2]/div/span/span")
nextButton.click()

time.sleep(4)

userPasswordInput = driver.find_element(By.XPATH, "//input[contains(@autocomplete,'current-password')]")
userPasswordInput.send_keys("SHa.arun*99#")

nextButton = driver.find_element(By.XPATH, "//div[contains(@role,'button')]/div/span/span")
nextButton.click()

explore_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/explore')]/div/div"))
)

# Scroll to the element
driver.execute_script("arguments[0].scrollIntoView();", explore_button)

# Use ActionChains to perform the click action
actions = ActionChains(driver)
actions.move_to_element(explore_button).click().perform()

time.sleep(4)

search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//form[contains(@role,'search')]"))
)
search_box.send_keys("python")

driver.quit()
