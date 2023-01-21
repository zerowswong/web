from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()

options.chrome_executable_path= "C:/Users/Zero/Desktop/chromedriver.exe"

driver = webdriver.Chrome(options = options)

driver.get("http://tsj.tw/")

clickd = driver.find_element(By.ID,"click")
count = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')
items = []
items.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]/i'))
items.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]/i'))
items.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]'))
prices = []

prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))
prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))
print(count.text)

actions = ActionChains(driver)




for i in range(10000):
   actions.click(clickd)
   actions.perform()
   countint = int(count.text.replace("您目前擁有","").replace("技術點",""))
   for j in range (3):
    price = int(prices[j].text.replace("技術點",""))
    if price <= countint :
        upgarde_actions = ActionChains(driver)
        upgarde_actions.move_to_element(items[j])
        upgarde_actions.click()
        upgarde_actions.perform()
       
    break




