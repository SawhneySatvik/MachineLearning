import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime("%Y-%m-%d")}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[ %(asctime)s ] %(lineno)d - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logger initialized")
    logging.debug("This is a debug message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")
    print(f"Logs are being saved to {LOG_FILE_PATH}")