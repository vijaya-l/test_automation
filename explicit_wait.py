import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
opx= webdriver.ChromeOptions()
opx.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opx)
driver.get("file:/Users/prao/PycharmProjects/test_automation/progress.html")
driver.maximize_window()

w=WebDriverWait(driver,40)
start=time.time()
driver.find_element("xpath",'//button[text()="Click Me"]').click()
locator=("xpath",'//div[text()="100%"]')
w.until(EC.presence_of_element_located(locator))
end=time.time()
print(end-start)
print("Done!!!")
driver.close()
#as soon as element present/visible on DOM , gives result output.