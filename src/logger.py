import logging
import os
from datetime import datetime

# Create a unique log file name using timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# ✅ Don't put "LOG_FILE" in quotes — use the variable itself
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)d] - %(message)s",
    level=logging.INFO,   # ✅ use logging.INFO (not logging.Info)
)

if __name__ == "__main__":
    try:
        a=1/10
    except Exception as e:
        logging.info("Loggin has started")
        raise CustomException(e,sys)
        