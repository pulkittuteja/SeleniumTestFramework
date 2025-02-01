import os

class Config:
    BROWSER = "edge"  # Set default browser
    URL = "https://parabank.parasoft.com/parabank/index.htm"  # Set default URL
    LOG_FILE = os.path.join(os.path.dirname(__file__), "../logs/test_log.log")  # Log file path

