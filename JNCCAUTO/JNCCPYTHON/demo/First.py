'''
Created on 23-Aug-2020

@author: LENOVO
'''
from selenium import webdriver

driver = webdriver.Chrome(r'D:\Automation\chromedriver.exe')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Index.html")
driver.find_element_by_id('email').send_keys("harishhariavi@gmail.com")
driver.find_element_by_id('enterimg').click()
driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("harish")
driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("avinash")