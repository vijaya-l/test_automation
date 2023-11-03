import time

from selenium import webdriver

opx= webdriver.ChromeOptions()
opx.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opx)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
#'Release Notes' is dependent on 'Python 3.9.8'
driver.find_element("xpath",'//a[text()="Python 3.9.8"]/../..//a[text()="Release Notes"]').click()
time.sleep(2)
