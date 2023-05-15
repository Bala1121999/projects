from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import credential

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://adactinhotelapp.com/index.php")
driver.find_element(By.LINK_TEXT,"New User Register Here").click()
driver.find_element(By.XPATH,"//input[@id='username']").send_keys(credential.Username)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys(credential.Password)
driver.find_element(By.XPATH,"//input[@id='re_password']").send_keys(credential.Password)
driver.find_element(By.XPATH,"//input[@id='full_name']").send_keys(credential.Full_Name)
driver.find_element(By.XPATH,"//input[@id='email_add']").send_keys(credential.Email_Address)
time.sleep(5)







