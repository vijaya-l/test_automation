from selenium import webdriver
from urllib import request

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument("--test-type")
# chrome_options.binary_location = "/usr/bin/chromium"

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://en.wikipedia.org/wiki/Thunderstorm')

heading1 = driver.find_element("class name", 'mw-file-description')
print(heading1)

images = driver.find_elements("tag name", "img")
for image in images:
    request.urlretrieve(image.get_attribute("src"))

driver.close()




# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Set the download directory and enable safe browsing
# download_directory = "/Users/prao/Documents/shivalli"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("prefs", {
#     "download.default_directory": download_directory,
#     "safebrowsing.enabled": True
# })
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://shivallikutumbana.org/executive-committee/")
#
# # Find all image elements on the page
# images = driver.find_elements(By.TAG_NAME, 'img')
#
# # Iterate through each image and click on it to trigger download
# for img in images:
#     time.sleep(2)  # Wait for the download to complete (adjust as needed)
#
# driver.quit()