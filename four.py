

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()


driver.get("https://w3schools.com/")

try:
    
    search_box = driver.find_element(By.ID,"search2")
    
    search_box.send_keys("html")
    
    search_box.send_keys(Keys.RETURN)
    
    # print(f"found element with name='username: {search_box}")
    
except Exception as e:
    print("error while locate the element", e)
    
    
driver.quit()