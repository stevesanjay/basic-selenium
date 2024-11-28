

# by xpath


from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()

driver.get("https://books.toscrape.com")



try:
    
    element = driver.find_element(By.XPATH,"//*[@id='default']/div/div/div/div/section/div[2]/ol/li[1]/article/div[2]/form/button")
    
    element.click()
    
    print(element)
    
except Exception as e:
    print("error while locate the element", e)
    
    
driver.quit()