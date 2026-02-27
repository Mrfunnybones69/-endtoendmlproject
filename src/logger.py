import logging
from pathlib import Path
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

LOG_DIR = Path.cwd() / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE_PATH = LOG_DIR / LOG_FILE

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)

if __name__ == "__main__":
    logging.info("Logging setup complete. This is a test log message.")
