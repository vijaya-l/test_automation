import time

from selenium import webdriver

opx= webdriver.ChromeOptions()
opx.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opx)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("css selector",'a[class="ico-register"]').click()
time.sleep(2)
driver.find_element("id","gender-male").click()
driver.find_element("id","FirstName" ).send_keys("Vijaya")
driver.find_element("id","LastName" ).send_keys("Rao")
driver.find_element("id","Email").send_keys("test@gmail.com")
driver.find_element("id","Password").send_keys("test123")
driver.find_element("id","ConfirmPassword").send_keys("test123")
driver.find_element("id","register-button" ).click()
time.sleep(3)
driver.close()