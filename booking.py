from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import credential


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://adactinhotelapp.com/index.php")
driver.find_element(By.XPATH,"//input[@id='username']").send_keys(credential.Username)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys(credential.Password)
driver.find_element(By.XPATH,"//input[@id='login']").click()
Location = Select(driver.find_element(By.XPATH,"//select[@id='location']"))
Location.select_by_visible_text("Brisbane")
hotel = Select(driver.find_element(By.XPATH,"//select[@id='hotels']"))
hotel.select_by_visible_text("Hotel Creek")
room_type = Select(driver.find_element(By.XPATH,"//select[@id='room_type']"))
room_type.select_by_visible_text("Deluxe")
No_rooms = Select(driver.find_element(By.XPATH,"//select[@id='room_nos']"))
No_rooms.select_by_value("2")
driver.find_element(By.XPATH,"//input[@id='datepick_in']").send_keys("15/05/2023")
driver.find_element(By.XPATH,"//input[@id='datepick_out']").send_keys("18/05/2023")
Apr = Select(driver.find_element(By.XPATH,"//select[@id='adult_room']"))
Apr.select_by_value("2")
Cpr = Select(driver.find_element(By.XPATH,"//select[@id='child_room']"))
Cpr.select_by_value("0")
driver.find_element(By.XPATH,"//input[@id='Submit']").click()
button = driver.find_element(By.XPATH, "//input[@id='radiobutton_0']")
Cnt = driver.find_element(By.XPATH,"//input[@id='continue']")
if button.is_displayed():
    button.click()
else:
    print("not selected")
if button.is_selected():
    Cnt.click()
else:
    print("not selected")
driver.find_element(By.XPATH,"//input[@id='first_name']").send_keys("test")
driver.find_element(By.XPATH,"//input[@id='last_name']").send_keys("test")
driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("test")
driver.find_element(By.XPATH,"//input[@id='cc_num']").send_keys("9876543456789876")
cct = Select(driver.find_element(By.XPATH,"//select[@id='cc_type']"))
cct.select_by_visible_text("American Express")
mnth = Select(driver.find_element(By.XPATH,"//select[@id='cc_exp_month']"))
mnth.select_by_visible_text("May")
year = Select(driver.find_element(By.XPATH,"//select[@id='cc_exp_year']"))
year.select_by_visible_text("2030")
driver.find_element(By.XPATH,"//input[@id='cc_cvv']").send_keys("6988")
driver.find_element(By.XPATH,"//input[@id='book_now']").click()
time.sleep(10)








