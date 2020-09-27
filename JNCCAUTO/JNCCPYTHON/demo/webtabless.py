'''
Created on 04-Sep-2020

@author: LENOVO
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
#open the first window
driver = webdriver.Chrome(r'D:\Automation\chromedriver.exe')
driver.maximize_window()
driver.get("https://techcanvass.com/examples/webtable.html")
trd=list(driver.find_elements_by_tag_name('td'))
for i in trd:
    print(i.text)
