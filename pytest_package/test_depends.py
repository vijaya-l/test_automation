import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(3)

import pytest
@pytest.mark.dependency()
def test_reg():
    driver.find_element("xpath",'//a[text()="Register"]').click()


@pytest.mark.dependency(depends=['test_reg'])
#if test_reg passed then test_names function is going to execute otherwise it gets skipped
def test_names():
    driver.find_element("id","FirstName").send_keys("Vijaya")
    driver.find_element("id", "LastName").send_keys("Lakshmi")