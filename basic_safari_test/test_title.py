from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Safari WebDriver
driver = webdriver.Safari()

try:
    # Step 1: Navigate to Google
    driver.get("https://www.google.com")

    # Step 2: Locate the search box using its name attribute
    search_box = driver.find_element(By.NAME, "q")

    # Step 3: Enter the search term and hit Enter
    search_box.send_keys("Sapphire Browser Automation" + Keys.RETURN)

    # Step 4: Wait for the results to load
    time.sleep(2)

    # Step 5: Print the title of the first result page
    print("Page title is:", driver.title)

    # Step 6: Find and print the URL of the first result
    first_result = driver.find_element(By.CSS_SELECTOR, "h3")
    print("First result title:", first_result.text)

finally:
    # Close the browser
    driver.quit()
