from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import credential

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://adactinhotelapp.com/index.php")
driver.find_element(By.XPATH,"//input[@id='username']").send_keys(credential.Username)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys(credential.Password)
driver.find_element(By.XPATH,"//input[@id='login']").click()
Title = driver.find_element(By.XPATH,"//span[@class='login_title_comm']")
if Title.is_displayed():
    print("Test case passed")
else:
    print("test case failed")
