#Assignment: Scenario: You’re testing a login feature. 
# - Write a Selenium script to: 
# 1. Navigate to the-internet.herokuapp.com/login
# 2. Enter username “tomsmith” and password “SuperSecretPassword!”
# 3. Click login
# 4. Verify “You logged into a secure area!” message
# - Use XPath/CSS selectors. Save as test_login.py in GitHub


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://the-internet.herokuapp.com/login'
print('Selenium running. Do hold on...')

def set_up():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.set_window_size(width=1920, height=1080)

    print('Driver automatically initialized successfully')
    return driver

def test_login():
    driver = set_up()
    try:
        # 1. Navigate to url
        driver.get(url)
        print('Webpage opened and verified successfully.')

        # 2. Enter username and password
        username_input = driver.find_element(By.ID, 'username')
        password_input = driver.find_element(By.ID, 'password')
        print('Username and password fields found successfully.')

        username_input.send_keys('tomsmith')
        password_input.send_keys('SuperSecretPassword!')
        print('Username and password entered successfully.')

        # 3. Click login
        login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login_button.click()
        print('Login button clicked successfully.')

        # 4. Verify “You logged into a secure area!” message
        flash = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'flash'))
        )
        if 'You logged into a secure area!' in flash.text:
            print('Successful and secure Login.!!! Welcome Aboard!!! ')
        else:
            print('Login not secure. Please try again.')


    except Exception as e:
        print(f'Failed to test login: {e}')
    
    finally:
        driver.quit()

if __name__ == '__main__':
    test_login()