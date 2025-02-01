import logging
from config.config import Config

# Configure logging
logging.basicConfig(
    filename=Config.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",  # Overwrites the log file each time
)

def get_logger():
    """
    Returns a configured logger instance.
    """
    return logging.getLogger()
