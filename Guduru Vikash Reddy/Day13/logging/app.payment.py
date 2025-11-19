import logging  # Import logging module

# Create logger for 'app.payment' and set level to WARNING
logger = logging.getLogger("app.payment")
logger.setLevel(logging.WARNING)

# Console handler with CRITICAL level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.CRITICAL)

# File handler with DEBUG level
file_handler = logging.FileHandler("app_payment.log")
file_handler.setLevel(logging.DEBUG)

# Define log formats
console_format = logging.Formatter("%(levelname)s | %(message)s|line:%(lineno)d")
file_format = logging.Formatter("%(message)s|%(levelname)s | %(message)s|")

# Apply formats to handlers
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Attach handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Log messages of various levels
logger.debug("this is a debug message (only on file)")
logger.info("this is a info message")
logger.warning("this is a warning message")
logger.error("this is a error message")

# Final message
print("Done! check app_payment.log for full logs")