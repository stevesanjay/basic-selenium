



# by name

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()


driver.get("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")

try:
    
    element = driver.find_element(By.NAME,"viewport")
    
    
    element.send_keys("my username")
    
    print(f"found element with name='username: {element}")
    
except Exception as e:
    print("error while locate the element", e)
    
    
driver.quit()