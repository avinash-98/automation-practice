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
driver.get("http://demo.automationtesting.in/Register.html")
driver.find_element_by_xpath('/html/body/section/div/div/div[2]/form/div[1]/div[1]/input').send_keys("harish")
a = ActionChains(driver)
a.send_keys(Keys.TAB,"avinasih",Keys.TAB,"vizag").perform()


    