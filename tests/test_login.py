import pytest
import json
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import get_logger

# Load credentials
CREDENTIALS_FILE = "data/credentials.json"
LOCATORS_FILE = "data/locators.json"

with open(CREDENTIALS_FILE, "r") as file:
    CREDENTIALS = json.load(file)

with open(LOCATORS_FILE, "r") as file:
    LOCATORS = json.load(file)


@pytest.mark.usefixtures("browser")
class TestLogin:

    @pytest.mark.parametrize("test_case", ["TC_007", "TC_008", "TC_009", "TC_010"])
    def test_login_invalid_credentials(self, browser, test_case):
        """
        Test login with invalid credentials.
        - TC_010: Empty username & password
        - Other cases: Incorrect credentials
        """
        logger = get_logger()
        driver = browser

        logger.info(f"Running Test Case: {test_case}")
        driver.get("https://parabank.parasoft.com/parabank/index.htm")

        # Extract credentials
        username = CREDENTIALS[test_case]["username"]
        password = CREDENTIALS[test_case]["password"]
        logger.info(f"Logging in with Username: '{username}' and Password: '{password}'")

        # Use locators from JSON
        driver.find_element(By.CSS_SELECTOR, LOCATORS["login_page"]["username"]).send_keys(username)
        driver.find_element(By.CSS_SELECTOR, LOCATORS["login_page"]["password"]).send_keys(password)
        driver.find_element(By.CSS_SELECTOR, LOCATORS["login_page"]["login_button"]).click()

        logger.info("Clicked on Login button.")

        # Wait for error message
        wait = WebDriverWait(driver, 10)
        error_element = wait.until(EC.presence_of_element_located((By.XPATH, LOCATORS["login_page"]["error_message"])))
        error_message = error_element.text
        logger.info(f"Error message displayed: {error_message}")

        # Assertions
        expected_error = "Please enter a username and password." if test_case == "TC_009" else "The username and password could not be verified."
        assert expected_error in error_message, f"Expected '{expected_error}', but got '{error_message}'"

        logger.info(f"Test {test_case} completed successfully")

    def test_login_positive(self, browser):
        """Test login with valid credentials"""
        logger = get_logger()
        driver = browser

        logger.info("Running Test Case: Valid Login")

        driver.get("https://parabank.parasoft.com/parabank/index.htm")

        valid_username = CREDENTIALS["valid"]["username"]
        valid_password = CREDENTIALS["valid"]["password"]

        logger.info(f"Using valid username: {valid_username}")

        driver.find_element(By.CSS_SELECTOR, LOCATORS["login_page"]["username"]).send_keys(valid_username)
        driver.find_element(By.CSS_SELECTOR, LOCATORS["login_page"]["password"]).send_keys(valid_password)
        logger.info("Entered credentials.")

        driver.find_element(By.CSS_SELECTOR, LOCATORS["login_page"]["login_button"]).click()
        logger.info("Clicked on Login button.")

        # Wait for account page link
        wait = WebDriverWait(driver, 10)
        try:
            element = wait.until(EC.presence_of_element_located((By.XPATH, LOCATORS["login_page"]["open_account_link"])))
            logger.info("Login successful - 'openaccount.htm' element found.")
        except TimeoutException:
            logger.error("Login may have failed. 'openaccount.htm' element not found as this is a test website, sometimes login occurs and sometimes not")
            pytest.fail("Login failed. Unable to locate 'openaccount.htm'.")
