import logging  # Logging module

# Logger setup
logger = logging.getLogger("app.customer")
logger.setLevel(logging.WARNING)

# Handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.CRITICAL)

file_handler = logging.FileHandler("app_customer.log")
file_handler.setLevel(logging.DEBUG)

# Formatters
console_format = logging.Formatter("%(levelname)s | %(message)s|line:%(lineno)d")
file_format = logging.Formatter("%(message)s|%(levelname)s | %(message)s|")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Attach handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Log messages
logger.debug("this is a debug message (only on file)")
logger.info("this is a info message")
logger.warning("this is a warning message")
logger.error("this is a error message")
logger.critical("this is crtical message")

print("Done! check app_customer.log for full logs")