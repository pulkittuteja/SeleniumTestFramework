from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utilities.logger import get_logger

logger = get_logger()

def setup_browser(browser: str):

    logger.info(f"Initializing browser: {browser}")

    try:
        if browser.lower() == "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-extensions")
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=chrome_options
            )

        elif browser.lower() == "firefox":
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install())
            )

        elif browser.lower() == "edge":
            driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install())
            )

        else:
            logger.error(f"Unsupported browser: {browser}")
            raise ValueError(f"Unsupported browser: {browser}")

        logger.info(f"Browser {browser} initialized successfully.")
        return driver

    except Exception as e:
        logger.error(f"Failed to initialize browser: {e}")
        raise
