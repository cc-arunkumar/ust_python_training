import logging

# # Create loggers
# payment_logger = logging.getLogger("app.payment")
# payment_logger.setLevel(logging.INFO)

customer_logger = logging.getLogger("app.customer")
customer_logger.setLevel(logging.INFO)

# Create handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

# Create formatters
console_format = logging.Formatter("%(levelname)s | %(message)s | line: %(lineno)d")
file_format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Attach handlers to both loggers
# payment_logger.addHandler(console_handler)
# payment_logger.addHandler(file_handler)

customer_logger.addHandler(console_handler)
customer_logger.addHandler(file_handler)

# Log messages using one of the loggers
customer_logger.debug("This is a DEBUG message (only file)")
customer_logger.info("This is an INFO message")
customer_logger.warning("This is a WARNING message")
customer_logger.error("This is an ERROR message")