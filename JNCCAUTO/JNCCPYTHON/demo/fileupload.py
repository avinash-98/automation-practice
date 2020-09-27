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
driver.get("http://demo.automationtesting.in/FileUpload.html")
driver.find_element_by_id('input-4').send_keys(r'C:\Users\LENOVO\Desktop\download.jpg')
