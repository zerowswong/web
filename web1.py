import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = Options()

options.chrome_executable_path= "C:/Users/Zero/Desktop/chromedriver.exe"

driver = webdriver.Chrome(options = options)

driver.get("http://www.ptt.cc/bbs/Stock/index.html")

# print(driver.page_source)

tags = driver.find_elements(By.CLASS_NAME,"title")
print(driver.title)
for tag in tags:
    print(tag.text)

link = driver.find_element(By.LINK_TEXT,"‹ 上頁")
link.click()


# WebDriverWait(driver,10).until(
#      EC.presence_of_element_located((By.LINK_TEXT,"聯絡我們"))
# )


tags = driver.find_elements(By.CLASS_NAME,"title")
print(driver.title)
for tag in tags:
    print(tag.text)

driver.close()

# driver.get("https://tvb.com/")
# print(driver.title)

# titles = driver.find_element("class name", "ant-image-img")
# for title in titles:
#     print(title.text)
# search = driver.find_element("name","keyword")
# search.click()
# search.clear()
#
# search.send_keys("abc")
#
# search.send_keys(Keys.RETURN)


# quit time
# while True:
#     time.sleep(0.1)
