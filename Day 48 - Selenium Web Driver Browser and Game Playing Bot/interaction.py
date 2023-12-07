from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

#driver = webdriver.Chrome(chrome_options)
#driver.get('https://en.wikipedia.org/wiki/Main_Page')


driver = webdriver.Chrome()
driver.get('http://secure-retreat-92358.herokuapp.com/')

search = driver.find_element(By.XPATH,'/html/body/form/input[1]')
search.send_keys('Shankar')
search.send_keys(Keys.ENTER)

search1 = driver.find_element(By.XPATH,'/html/body/form/input[2]')
search1.send_keys('Narayan')
search1.send_keys(Keys.ENTER)

search2 = driver.find_element(By.XPATH,'/html/body/form/input[3]')
search2.send_keys('123@gmail.com')
search2.send_keys(Keys.ENTER)

search2 = driver.find_element(By.XPATH,'/html/body/form/button')
search2.click()


