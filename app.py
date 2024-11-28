'''
Created on 

@author: Steve
source:
    
'''



from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# driver.get("")


INPUT_FILENAME = "input_baseurl.txt"

config = {
    "link" : "div.page_inner div section ol.row li h3 a"
}

def get_file_content():
    with open(INPUT_FILENAME,'r',encoding='utf-8') as text_file:
        return [line.strip() for line in text_file]
    
def get_custom_elements(review_url):
    
    driver.get(review_url) 
    
    driver_link_list = driver.find_elements(By.CSS_SELECTOR, config['link'] )
    
    link_list = []
    
    for dlink in driver_link_list:
        
        href_value = dlink.get_attribute("href")
        
        link_list.append(href_value)
        
    return link_list

def link2file(links):
    
    with open("booklinks.txt","a") as f:
        for link in links:
            f.write(f"{link}\n")

def startpy():

    link_urls = get_file_content()
    # print(link_urls)
    
    
    for c_url in link_urls:
        list_links = get_custom_elements(c_url)
        
        link2file(list_links)
        
        print(f"{len(list_links)} links added successfully")
        
    driver.quit()


if __name__ == '__main__':
    startpy()