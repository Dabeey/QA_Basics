from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

print('Setting up Selenium WebDriver automatically...')

def setup_selenium():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Make Chrome run without showing a browser window
    options.add_argument("--no-sandbox") #Turn off Chrome’s security sandbox to avoid crashes in some environments
    options.add_argument("--disable-dev-shm-usage") # Stop Chrome from using shared memory to prevent crashes in low-memory setups
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="latest").install()), options=options)
    print('Driver automatically initialized successfully')

    driver.get("https://google.com")

    # Find the search box using its name attribute value
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys('Get It Done!') # Enter the search query
    search_box.submit()

    # Wait for the page to load
    time.sleep(2)
    print(driver.title) # Print the title of the page to confirm it loaded correctly

    return driver

if __name__ == "__main__":
    driver = setup_selenium()
    driver.quit()  # Close the browser after the task is done