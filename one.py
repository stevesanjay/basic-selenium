

# by id 

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


driver.get("https://books.toscrape.com")

try:
    
    element = driver.find_element(By.ID,"promotions_left")
    
    find_element = element.text
    print(find_element)
    
except Exception as e:
    print("error while locate the element", e)
    
    
driver.quit()