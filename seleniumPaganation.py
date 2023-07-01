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
driver.get("https://www.audible.com/search")

pagination = driver.find_elements(By.XPATH,"//ul[contains(@class,'pagingElements')]/li")
first_page = int(pagination[1].text)
second_last_page = int(pagination[-2].text)
last_page = pagination[-1]
next_button =last_page.find_element(By.XPATH,"./span[contains(@class,'nextButton')]") 

title = []
author = []
narrator = []
runTime = []
while first_page <= second_last_page:
    time.sleep(2)
    container = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,"center-3")))
    products = WebDriverWait(container,5).until(EC.presence_of_all_elements_located((By.XPATH,"./div/div/div/span/ul/li")))
    # container = driver.find_element(By.ID,"center-3")
    # products = container.find_elements(By.XPATH,"./div/div/div/span/ul/li")
    for product in products:
        title.append(product.find_element(By.XPATH,".//h3[contains(@class,'bc-heading')]").text)
        author.append(product.find_element(By.XPATH,".//li[contains(@class,'authorLabel')]").text)
        narrator.append(product.find_element(By.XPATH,".//li[contains(@class,'narratorLabel')]").text)
        runTime.append(product.find_element(By.XPATH,".//li[contains(@class,'runtimeLabel')]").text)
    first_page += 1
    try:
        next_button.click()
    except:
        pass

df = pd.DataFrame({"Title":title,"Author":author,"Narrator":narrator,"RunTime":runTime})
df.to_csv("BooksDetailsImplicit.csv",index=False)
driver.quit()