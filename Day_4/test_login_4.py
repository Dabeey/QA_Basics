# Assignment: 
# Scenario: You’re organizing tests for a client. 
#  - Convert your Day 3 login script into a Pytest test case. 
#  - Add 2 more test cases: 
    # 1. Invalid username (expect error)
    # 2. Invalid password (expect error). 
#  - Save as test_login_pytest.py in GitHub. 
#  - Run with pytest -v. 
#  - Expected: 3 tests run (1 pass, 2 fail as expected).

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()


# ✅ Test 1: Valid Login
def test_valid_login(driver):
    try:
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        assert "You logged into a secure area!" in message.text

    except Exception as e:
        take_screenshot(driver, "valid_login_failed.png")
        pytest.fail(f"Valid login test failed: {e}")


# ❌ Test 2: Invalid Username
def test_invalid_username(driver):
    try:
        driver.find_element(By.ID, "username").send_keys("wronguser")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        assert "Your username is invalid!" in message.text

    except Exception as e:
        take_screenshot(driver, "invalid_username_failed.png")
        pytest.fail(f"Invalid username test failed: {e}")


# ❌ Test 3: Invalid Password
def test_invalid_password(driver):
    try:
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("wrongpassword")
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        assert "Your password is invalid!" in message.text

    except Exception as e:
        take_screenshot(driver, "invalid_password_failed.png")
        pytest.fail(f"Invalid password test failed: {e}")


# 📸 Utility function to take screenshots on failure
def take_screenshot(driver, filename):
    driver.save_screenshot(filename)
    print(f"📸 Screenshot saved as: {filename}")


if __name__ == '__main__':
    pytest.main(["-v", __file__])
# Run this script with pytest -v to see the results of the tests.
