import time
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.get("file:/Users/prao/PycharmProjects/test_automation/demo.html")
driver.maximize_window()
time.sleep(2)
#driver.find_element("xpath",'//td[text()="Java"]/..//input[@type="checkbox"]').click()
#multiple check box
languages=["Java","Ruby","Perl","Python","C#","JavaScript"]
for language in languages:
    driver.find_element("xpath",f'//td[text()="{language}"]/..//input[@type="checkbox"]').click()
driver.close()