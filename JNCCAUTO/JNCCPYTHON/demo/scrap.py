'''
Created on 04-Sep-2020

@author: LENOVO
'''
from selenium import webdriver
driver = webdriver.Chrome(r'D:\Automation\chromedriver.exe')
driver.get('http://demo.automationtesting.in/Register.html')
wait=new WebdriverWait(driver,30)
wait.until(ExpectedConditions.element_to_be_clickable(By.xpath("//butoon")))
#driver.implicitly_wait(7000);
print(driver.title)
driver.implicitly_wait(7000);
print(driver.title)

