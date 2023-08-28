from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

#opciones

options= webdriver.ChromeOptions()
options.add_argument ('--incognito')

#controlador

driver_service =Service (ChromeDriverManager().install())
driver=webdriver.Chrome(service=driver_service, options=options)

#instragram
driver.get('https://www.instagram.com')

sleep(5)

username_input = driver.find_element (By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
password_input = driver.find_element (By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')

username_input.send_keys('usuario')
password_input.send_keys('12345678')
sleep (10)

login_button = driver.find_element (By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
login_button.click()

sleep(5)