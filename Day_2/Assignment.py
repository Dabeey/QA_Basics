#Assignment: Scenario: You’re testing a blog site. 
# - Write a Python script using Selenium to: 1. Open the-internet.herokuapp.com, 2. Verify the page title is “The Internet.” 
# - Save as test_open_page.py in your GitHub repo. 
# - Expected: Script runs without errors, prints “Title verified” if correct.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

print('Setting up Selenium WebDriver automatically...')

def set_up():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager(driver_version="138.0.7204.168").install()),
            options=options
        )
        print('Driver automatically initialized successfully')

        # 1. Open the-internet.herokuapp.com
        driver.get('https://the-internet.herokuapp.com')
        time.sleep(2)
        print('Webpage opened and verified successfully.')
        return driver
    except Exception as e:
        print(f'[ERROR] Failed to set up Selenium WebDriver: {e}')
        return None
    

def test_open_page():
    # Open Page
    driver = set_up()
    result = ""
    if driver is None:
        result = "[ERROR] WebDriver not initialized."
    else:
        try:
            title = driver.title
            print(f'Title of the page: {title}')
            if title == 'The Internet':
                result = "Title verified!"
            else:
                result = "Title not verified!"
        except Exception as e:
            result = f"[ERROR] Failed to verify title: {e}"
        finally:
            driver.quit()
    # Write result to a new file
    with open('../title_verification_result.txt', 'w') as file:
        file.write(result + "\n")
    return result


# run script file
if __name__ == '__main__':
    set_up()
    test_open_page()