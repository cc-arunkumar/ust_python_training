import logging

logger = logging.getLogger("app_payment")
logger.setLevel(logging.DEBUG)

# Handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

file_handler = logging.FileHandler("app_payment.log")
file_handler.setLevel(logging.WARNING)

# Formatters
console_format = logging.Formatter("%(levelname)s | %(message)s | line : %(lineno)d")
file_format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add handlers (not formatters!)
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Test logs
logger.debug("This is a debug message !")
logger.info("This is a info message.")
logger.warning("This is a warning message.")
logger.error("This is a error message.")
