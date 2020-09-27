'''
Created on 28-Aug-2020

@author: LENOVO
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(r'D:\Automation\chromedriver.exe')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Alerts.html")

driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[3]/button').click()
driver.implicitly_wait(10)

driver.switch_to_alert().send_keys('hello hari').accept()

driver.implicitly_wait(10)



