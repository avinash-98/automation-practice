'''
Created on 28-Aug-2020

@author: LENOVO
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(r'D:\Automation\chromedriver.exe')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Frames.html")

driver.find_element_by_xpath('/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a').click()
driver.switch_to.frame(1)
print("hello")
driver.switch_to.frame(0)
driver.implicitly_wait(30)

driver.find_element_by_css_selector('body > section > div > div > div > input[type=text]').send_keys('hi')
driver.switch_to.default_content()
print(driver.find_element_by_xpath('/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a').text)


