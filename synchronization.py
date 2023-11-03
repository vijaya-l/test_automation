"""
2 types
1. unconditional : time.sleep()
    - make interpreter to wait for "n" seconds

2. conditional sync : makes driver to wait until some condition is met externally

implicit wait - it wait until the element is located on DOM page
explicit wait - condition will be specified externally
"""
import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get("file:/Users/prao/PycharmProjects/test_automation/loading.html")
driver.maximize_window()

# first_name = driver.find_element("name", "fname")
# print(first_name)
# time.sleep(10)
# first_name.send_keys("steeve")
#
# last_name = driver.find_element("name", "lname")
# print(last_name)
# last_name.send_keys("john")

# unconditional
# initialize the driver with implicit wait of n sec
# driver.implicitly_wait(10)  # one impl wait should be used for entire web element
# driver.find_element("name", "fname").send_keys("steeve")
# time.sleep(2)

# driver.find_element("name", "fname").send_keys("steeve")
start = time.time()
driver.implicitly_wait(20)
driver.find_element("name", "fname").send_keys("steeve")
end = time.time()
print(end - start)
time.sleep(2)

driver.close()