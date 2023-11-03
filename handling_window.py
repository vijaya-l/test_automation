import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.implicitly_wait(20)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("link text","Facebook").click()
handles=driver.window_handles
driver.switch_to.window(handles[1])
