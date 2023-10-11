import time

from selenium import webdriver

#driver=webdriver.Chrome()
#driver.get("https://demowebshop.tricentis.com/")
#if session is closed automatically,then use this snippet
opx= webdriver.ChromeOptions()
opx.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opx)
driver.get("https://demowebshop.tricentis.com/")
driver.find_element("id","small-searchterms").send_keys("Hello")
time.sleep(2)
driver.find_element("name","q").clear()