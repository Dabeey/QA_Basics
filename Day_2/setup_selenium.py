from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

print('Setting up Selenium WebDriver automatically...')

def setup_selenium():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    options.add_argument("--no-sandbox") 
    options.add_argument("--disable-dev-shm-usage") 
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="138.0.7204.168").install()), options=options)
    print('Driver automatically initialized successfully')

    driver.get("https://google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys('Get It Done!')
    search_box.submit()

    time.sleep(2)
    title = driver.title
    print(f'DRIVER TITLE: \n {title}') # Print the title of the page to confirm it loaded correctly

    return driver

if __name__ == "__main__":
    driver = setup_selenium()
    driver.quit()  