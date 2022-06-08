import time
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

url = 'https://warframe.market'
s = Service("/Users/User/PycharmProjects/test/chromedriver.exe")
driver = webdriver.Chrome(service=s)
searchXPath = '//*[@id="panel"]/section[1]/div[1]/section/div/section/div/section/span/input'

wait = WebDriverWait(driver, 5)

modFile = open('modList.txt', 'r')
modList = []
for line in modFile:
    strippedLine = line.strip()
    modList.append(strippedLine)
def driverInit():
    driver.get(url)

def searchMod(driver, mod):
    search = driver.find_element(By.XPATH, searchXPath)
    print('searching for %s' % mod)
    for i in range(20):
        search.send_keys(Keys.BACK_SPACE)
    search.send_keys(mod)
    search.send_keys(Keys.RETURN)
    time.sleep(2)


def clickButton(driver, elementName, elementText):
    buttons = driver.find_elements(By.CLASS_NAME, elementName)
    for button in buttons:
        if button.text == elementText:
            button.click()

def findPrice(driver):
    wait.until(presence_of_element_located((By.CLASS_NAME, 'item__name')))

    driver.execute_script("window.scrollTo(0, 300)")

    sellPriceInt = 0
    buyPriceInt = 0
    buttonClass = 'btn__primary--L8HyD'

    clickButton(driver, buttonClass, 'Maxed')
    clickButton(driver, buttonClass, 'Sellers')

    try:
        sellPrice = driver.find_element(By.CLASS_NAME, "platinum-price--DQ63t")
        sellPriceInt = int(sellPrice.text)
        print('Lowest Sell Price: ')
        print(sellPriceInt)
    except:
        print("Could not Find Price!")

    clickButton(driver, buttonClass, 'Buyers')
    try:
        buyPrice = driver.find_element(By.CLASS_NAME, 'platinum-price--DQ63t')
        buyPriceInt = int(buyPrice.text)
        print('Highest Buy Price: ')
        print(buyPriceInt)
    except:
        print('Could not Find Price!')
    statisticClass = 'smartLink--182DB'

    print("Price Spread: ")
    print(sellPriceInt - buyPriceInt)

    driver.execute_script("window.scrollTo(0, 500)")
    # clickButton(driver, statisticClass, 'STATISTICS')
    # volumeIndexList = [89, 88, 87]
    # for volumeIndex in volumeIndexList:
    #
    #     volumePath = '//*[@id="svg-prices-new"]/svg/g/g[2]/g[4]/rect[89]'
    #     volume = driver.find_element(By.XPATH, volumePath)
    #     print('volume property: ', volume.get_property())
if __name__ == '__main__':
    driverInit()
    #print(modList)
    mod = modList[0]
    searchMod(driver, mod)
    findPrice(driver)
    for mod in modList:
       searchMod(driver, mod)
       findPrice(driver)

    driver.quit()

