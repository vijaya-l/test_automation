"""
to automate low level interaction like mouse movements, mouse buttons, press keys

import actionchains class
create an object for Actionchain class
"""
import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

# driver.get("https://www.myntra.com/")
# driver.maximize_window()

from selenium.webdriver.common.action_chains import ActionChains
act_obj = ActionChains(driver)
# # link = driver.find_element("xpath", '//div[@class="desktop-navLink"]//a[text()="Men"]')
# # act_obj.move_to_element(link).perform()
#
# profile = driver.find_element("xpath", '//span[text()="Profile"]')
# act_obj.move_to_element(profile).perform()
# time.sleep(2)

############################################################################################################
# double click and page down
# from selenium.webdriver.common.keys import Keys
# driver.get("file:///C:/Users/Lenovo/Desktop/website/demo.html")
# driver.maximize_window()
#
# button = driver.find_element("id", "double-click")
# act_obj.double_click(button).perform()
#
# act_obj.send_keys(Keys.PAGE_DOWN).perform()
#
# time.sleep(2)

################################################################################################
#drag and drop
driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
driver.maximize_window()

draggable = driver.find_element("id", "draggable")
droppable = driver.find_element("id", "droppable")

act_obj.drag_and_drop(draggable, droppable).perform()
time.sleep(5)


#################################################################################################3
# file upload
# driver.get("file://Users/prao/PycharmProjects/test_automation/demo.html")
# driver.maximize_window()
#
# path = r"C:\Users\Lenovo\Desktop\sample.docx"
# driver.find_element("xpath", '//input[@type="file"]').send_keys(path)
#
# time.sleep(10)
driver.close()