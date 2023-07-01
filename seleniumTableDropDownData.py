import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

os.environ["PATH"] += r"C:\FireFoxSelenium"
driver = webdriver.Firefox()
driver.get("https://www.adamchoi.co.uk/overs/detailed")
all_matches = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches.click()

dropdown = Select(driver.find_element(By.ID,"country"))
dropdown.select_by_visible_text("Spain")
time.sleep(4)


all_rows = driver.find_elements(By.TAG_NAME,"tr")

dates = []
palaces = []
scores = []
names = []
for rows in all_rows:
    dates.append(rows.find_element(By.XPATH,"./td[1]").text)
    palaces.append(rows.find_element(By.XPATH,"./td[2]").text)
    scores.append(rows.find_element(By.XPATH,"./td[3]").text)
    names.append(rows.find_element(By.XPATH,"./td[4]").text)

driver.quit()
print(dates)
print(palaces)
print(scores)
print(names)

df = pd.DataFrame({'Dates':dates,'Palacs':palaces,'Scores':scores,'names':names})
df.to_csv('footballListsSpain.csv',index = False)
print(df)

