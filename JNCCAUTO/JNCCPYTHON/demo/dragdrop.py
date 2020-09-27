'''
Created on 30-Aug-2020

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
'''driver.get("http://demo.automationtesting.in/Static.html")
source = driver.find_element_by_xpath('//*[@src="selenium.png"]')
target = driver.find_element_by_id("droparea")
# Create the object for Action Chains
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()'''

driver.get('https://jqueryui.com/droppable/')
driver.switch_to.frame(0)
src=driver.find_element_by_id('draggable')
tgt=driver.find_element_by_id('droppable')
actions = ActionChains(driver)
actions.drag_and_drop(src, tgt).perform()
