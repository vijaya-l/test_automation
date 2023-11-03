import time

from selenium import webdriver

opx= webdriver.ChromeOptions()
opx.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opx)
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()
driver.find_element("css selector",'tr input[name="username"]').send_keys("steve")
driver.find_element("css selector",'td>input[name="pwd"]').send_keys("password")