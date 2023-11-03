import os
import requests
from selenium import webdriver

# Specify the path to your ChromeDriver executable
driver = webdriver.Chrome(executable_path='/Users/prao/PycharmProjects/test_automation/Shivlli')

# Navigate to the webpage
driver.get("https://example.com")

# Find all image elements on the page
img_elements = driver.find_elements_by_tag_name('img')

# Create a directory to save the images
os.makedirs('downloaded_images', exist_ok=True)

# Download each image
for index, img in enumerate(img_elements):
    img_url = img.get_attribute('src')
    if img_url:
        img_name = f'downloaded_images/image_{index}.jpg'  # You can change the naming logic

        # Make a request to download the image
        response = requests.get(img_url)

        if response.status_code == 200:
            with open(img_name, 'wb') as f:
                f.write(response.content)
                print(f"Downloaded: {img_name}")
        else:
            print(f"Failed to download: {img_name}")

# Close the WebDriver
driver.quit()
