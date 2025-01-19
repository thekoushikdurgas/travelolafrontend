import logging
import sys
from logging.handlers import RotatingFileHandler

# Configure the logger
logger = logging.getLogger("project_logger")
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler(sys.stdout)
file_handler = RotatingFileHandler(
    "project.log", maxBytes=5 * 1024 * 1024, backupCount=3
)  # Rotates log files at 5 MB with 3 backups

# Set logging levels
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)

# Create formatters and add them to the handlers
formatter = logging.Formatter(
    "%(message)s"
    # "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
