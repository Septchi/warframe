from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import sys

url = 'https://warframe.market/items/blind_rage'
s = Service("/Users/User/PycharmProjects/test/chromedriver.exe")
#chromeDriverPath = "/Users/User/PycharmProjects/test/chromedriver.exe"
driver = webdriver.Chrome(service=s)
driver.get(url)
driver.implicitly_wait(5)

modsList = ['']

buttons = driver.find_elements(By.CLASS_NAME, "btn__primary--Rchh6")
for button in buttons:
    #print(button.text)
    if button.text == 'Maxed':
        button.click()
        print("clicked")
driver.implicitly_wait(5)
sellPrice = driver.find_element(By.CLASS_NAME, "platinum-price--3tqTy")
sellPriceInt = int(sellPrice.text)
print('Cheapest Sell Price: ')
print(sellPriceInt)

buttons = driver.find_elements(By.CLASS_NAME, "btn__primary--Rchh6")
for button in buttons:
    #print(button.text)
    if button.text == 'Buyers':
        button.click()
        print("clicked")
buyPrice = driver.find_element(By.CLASS_NAME, 'platinum-price--3tqTy')
buyPriceInt = int(buyPrice.text)

print('Cheapest Buy Price: ')
print(buyPriceInt)
print("Price Spread: ")
print(sellPriceInt - buyPriceInt)
search = driver.find_element(By.XPATH, '//*[@id="panel"]/section[1]/div[1]/section/div/section/div/section/span/input')
print(search)
driver.quit()


