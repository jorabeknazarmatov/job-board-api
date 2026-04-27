import logging
from pathlib import Path


current_path = Path(__file__).resolve()
BASE_DIR = current_path.parent.parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)


logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

file_log = logging.FileHandler(str(LOG_DIR / "app.log"))
console_log = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s || %(levelname)s || %(filename)s:%(lineno)s || %(message)s", datefmt="%d-%m-%Y %H:%M:%S")

file_log.setFormatter(formatter)
console_log.setFormatter(formatter)

logger.addHandler(file_log)
logger.addHandler(console_log)