from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time 

driver  = webdriver.Chrome()
driver.get("http://www.python.org")

element=driver.find_element(By.NAME,  "q")
element.clear()
element.send_keys("version")
element.send_keys(Keys.RETURN)
time.sleep(9)
driver.quit()