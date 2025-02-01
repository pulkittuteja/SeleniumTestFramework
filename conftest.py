import pytest
from utilities.browser_setup import setup_browser
from config.config import Config
from utilities.logger import get_logger

logger = get_logger()

@pytest.fixture(scope="class")
def browser():
    """
    Pytest fixture to set up and tear down the Selenium WebDriver.
    """
    logger.info("Starting test execution.")

    driver = setup_browser(Config.BROWSER)

    # Open the URL
    logger.info(f"Opening URL: {Config.URL}")
    driver.get(Config.URL)
    driver.maximize_window()

    # Yield driver to the test case
    yield driver

    # Teardown
    logger.info("Closing browser.")
    driver.quit()
    logger.info("Test execution completed.")
