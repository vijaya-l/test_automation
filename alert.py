import time

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath",'//input[@value="Search"]').click()
time.sleep(3)
alert_obj=driver.switch_to.alert
alert_obj.accept()