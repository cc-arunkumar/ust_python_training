import logging
from logging.handlers import RotatingFileHandler
import os
from app.core.config import settings

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "app.log")

logger = logging.getLogger("ust")
logger.setLevel(getattr(logging, settings.log_level.upper(), logging.INFO))

fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(fmt)
logger.addHandler(ch)

fh = RotatingFileHandler(LOG_FILE, maxBytes=5_000_000, backupCount=3)
fh.setFormatter(fmt)
logger.addHandler(fh)

def get_logger():
    return logger
