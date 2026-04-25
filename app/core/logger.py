import logging


logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

file_log = logging.FileHandler("app.log")
console_log = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s || %(levelname)s || %(filename)s:%(lineno)s || %(message)s", datefmt="%d-%M-%Y %H:%M:%S")

file_log.setFormatter(formatter)
console_log.setFormatter(formatter)

logger.addHandler(file_log)
logger.addHandler(console_log)