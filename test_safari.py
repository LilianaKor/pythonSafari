
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Safari WebDriver
driver = webdriver.Safari()

try:
    # Navigate to a website
    driver.get("https://www.example.com")

    # Find an element and interact with it
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Safari WebDriver" + Keys.RETURN)

    # Wait for results to load
    time.sleep(2)

    # Print the title of the page
    print(driver.title)

finally:
    # Close the browser
    driver.quit()
