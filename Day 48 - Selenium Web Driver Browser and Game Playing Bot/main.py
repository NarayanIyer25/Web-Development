from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

dict_data = {
0:{'time':driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time').text,
   'name':driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/a').text
   },
1:{
    'time':driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[2]/time').text,
    'name':driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[2]/a').text
    },
2:{
    'time':driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[3]/time').text,
    'name':driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[3]/a').text
    },
3:{
    'time':driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[4]/time').text,
    'name':driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[4]/a').text
    },
4:{
    'time':driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[5]/time').text,
    'name':driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[5]/a').text
    },

}

print(dict_data)

driver.close()