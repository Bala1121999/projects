from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/datepicker/#Icon%20Trigger")
driver.maximize_window()
driver.implicitly_wait(10)
year = "2027"
Month = "November"
day = "19"
frame_1 = driver.find_element(By.XPATH,"(//p//iframe)[1]")
driver.switch_to.frame(frame_1)
# #driver.find_element(By.XPATH,"//*[@id='Simple Date Picker']").click()
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
while True:
    yar = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    mnt = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text

    if yar == year and mnt == Month:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

days = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")

for d in days:
    if d.text == day :
        d.click()
        break




