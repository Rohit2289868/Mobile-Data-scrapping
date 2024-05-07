from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("E:/Data Science Mentorship Program By Nitish Sir/DSMP 1.0/Projects/10. Advanced Web Scrapping/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=s)

driver.get('https://www.smartprix.com/mobiles')
time.sleep(2)

# driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click() # click on out_of_stock checkbox
# time.sleep(2)
#
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click() # click on exclude upcoming checkbox
# time.sleep(2)

old_height = driver.execute_script('return document.body.scrollHeight')
count = 0
while True:

    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[3]/div[3]').click()
    
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')
    count = count + 1
    print("Count = ", count)
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source  # it will fetch all the html code

time.sleep(100)

# with open('mobile.html','w',encoding='utf-8') as f:
#     f.write(html)