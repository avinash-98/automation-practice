'''
Created on 28-Aug-2020

@author: LENOVO
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(r'D:\Automation\chromedriver.exe')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")

#get text from web page





'''
driver.find_element_by_xpath("//input[@value='FeMale']").click()
#clicking on checkboxes

driver.find_element_by_id('checkbox2').click()
'''

select = Select(driver.find_element_by_id('yearbox'))

# select by visible text
#select.select_by_visible_text('Croatia')

# select by value 
select.select_by_value('1920')
select1 = Select(driver.find_element_by_css_selector('#basicBootstrapForm > div:nth-child(11) > div:nth-child(3) > select'))
select1.select_by_visible_text('May')
select2 = Select(driver.find_element_by_id('daybox'))
select2.select_by_index(8)

