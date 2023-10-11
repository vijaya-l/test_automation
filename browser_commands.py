import time

from selenium import webdriver

opx= webdriver.ChromeOptions()
opx.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opx)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(2)
driver.minimize_window()
driver.fullscreen_window()
print(driver.get_window_size())
print(driver.get_window_rect())
#navigate in browser
driver.set_window_rect(100,200,300,400)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.quit()