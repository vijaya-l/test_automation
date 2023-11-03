from selenium import webdriver

opx= webdriver.ChromeOptions()
opx.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opx)
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()

#xpath: '//tag-name[@attribute="value"]'

driver.find_element("xpath",'//input[@id="username"]').send_keys("Test")
driver.find_element("xpath",'//input[@name="pwd"]').send_keys("test123")
