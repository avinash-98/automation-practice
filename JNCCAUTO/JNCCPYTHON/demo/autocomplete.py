'''
Created on 02-Sep-2020

@author: LENOVO
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r'D:\Automation\chromedriver.exe')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/AutoComplete.html")
driver.find_element_by_id('searchbox').send_keys("Ind")
a = ActionChains(driver)
for i in range(4):
    a.send_keys(Keys.DOWN).perform()
a.send_keys(Keys.ENTER).perform()