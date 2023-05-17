from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[normalize-space()='Click Me']").click()
alt = driver.switch_to.alert
print(alt.text)
alt.accept()
driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
sug = driver.find_elements(By.XPATH,"//a[contains(@href,'Selenium')]")
print(len(sug))
for i in sug:
    i.click()
id = driver.window_handles

for j in id:
    driver.switch_to.window(j)
    print(driver.title)
for c in id:
    driver.switch_to.window(c)
    driver.close()


time.sleep(5)
