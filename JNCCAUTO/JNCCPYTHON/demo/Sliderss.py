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
driver.get("http://demo.automationtesting.in/Slider.html")
slider = driver.find_element_by_id('slider')

Actions = ActionChains(driver)
Actions.click_and_hold(slider).move_by_offset(40,40).release().perform()
Actions.context_click(slider).perform()
