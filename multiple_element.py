import time

from selenium import webdriver

opx= webdriver.ChromeOptions()
opx.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opx)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
#elements=driver.find_elements("xml",'//div[@class="footer-menu-wrapper"]//a')
#for element in elements:
    #print(element.text)

links= driver.find_elements("tag name","a")
print(len(links))
for link in links:
    print(link.text)
    print(link.get_property("href"))

time.sleep(2)
driver.close()