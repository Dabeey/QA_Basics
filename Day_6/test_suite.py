# Assignment: Scenario: You’re testing a web app’s core features. 
#  - Automate: 
        # 1. Login test (from Day 3)
        # 2. Form submission 
        # 3. Navigate to “Checkboxes” and toggle a checkbox. 
#  - Use Pytest, save as test_suite.py. 
#  - Push to GitHub with README explaining setup and tests. 
#  - Expected: 3 passing tests in repo.


####################### IMPORTS ####################
# pytest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASEURL = 'https://the-internet.herokuapp.com'
print('Selenium running. Please, hold on...')

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm')

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    print('Driver automatically initialized successfully')

    driver.set_window_size(width=1920, height=1080)
    driver.get(BASEURL + '/login')
    yield driver

    driver.quit()
    print("Driver closed successfully")


def take_screenshot(driver, filename):
    driver.save_screenshot(filename)
    print(f'Screenshot saved as {filename}')


def test_valid_login(driver):
    try:
        # 1. Login test (from Day 3)
        driver.find_element(By.ID, 'username').send_keys('tomsmith')
        driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        driver.find_element(By.CSS_SELECTOR, 'button.radius').click()

        message = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'flash'))).text
        assert 'You logged into a secure area!' in message
        print("Login test passed")

    except Exception as e:
        take_screenshot(driver, "login_error.png")
        pytest.fail(f"An error occured during login process: {e}")


def test_form_submission(driver):
    # 2. Form submission 
    try:
        driver.find_element(By.ID, 'username').send_keys('tomsmith')
        driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        driver.find_element(By.CSS_SELECTOR, 'button.radius').click()

        assert 'secure' in driver.current_url
        print("Login test passed")

    except Exception as e:
        take_screenshot(driver, "form_submission_error.png")
        pytest.fail(f"Could not submit form: {e}")


def test_toogle_checkboxes(driver):
    try:
        # 3. Navigate to “Checkboxes” and toggle a checkbox. 
        driver.get(BASEURL + '/checkboxes')

        checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
        assert len(checkboxes) > 0

        checkbox = checkboxes[0]
        initial_state = checkbox.is_selected()
        checkbox.click()

        assert checkbox.is_selected() != initial_state
        print('Successfully toggled checkbox')

    except Exception as e:
        take_screenshot(driver,'toggle_checkbox_error.png')
        pytest.fail(f'Error toggling checkbox: {e}')



# if __name__ == '__main__':
#     pytest.main(['-v',__file__])
#     print("All tests completed successfully.")