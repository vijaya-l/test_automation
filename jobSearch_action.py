import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.naukri.com/")
driver.maximize_window()

from selenium.webdriver.common.action_chains import ActionChains
act_obj = ActionChains(driver)
link = driver.find_element("class name", "nI-gNb-menuItems__anchorDropdown")
act_obj.move_to_element(link).perform()
driver.close()