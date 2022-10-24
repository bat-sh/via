from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

#initialize the driver
driver = webdriver.Chrome(r"C:\Users\USER\Downloads\chromedriver.exe")

#open facebook.com with chrome
driver.get("https://www.demoblaze.com/")

my_username ="MyUserName"
my_password = "MyPassword111"

sign_up_button = driver.find_element_by_id("signin2")
sign_up_button.click()

time.sleep(2)

username_input_box = driver.find_element_by_id("sign-username")
password_input_box = driver.find_element_by_id("sign-password")

username_input_box.clear()
password_input_box.clear()
username_input_box.send_keys(my_username)
time.sleep(2)
password_input_box.send_keys(my_password)
time.sleep(2)
sign_up_close_button = driver.find_element_by_id("btn btn-primary")
sign_up_close_button.click()
time.sleep(30)

#2

driver.get("https://www.demoblaze.com/prod.html?idp_=3")
time.sleep(2)
add_item_button = driver.find_element_by_class_name("btn btn-success btn-lg")
add_item_button.click()
time.sleep(30)


driver.get("https://www.demoblaze.com/cart.html")
time.sleep(2)
r = requests.get("https://www.demoblaze.com/cart.html")
print(r.json())
if r['number'] == 1 and r['price'] == 650 and r['title'] == "Nexus 6" and r['id'] == 3:
    print('ok')
time.sleep(30)
driver.close()
