import logging

logger = logging.getLogger("app.payment")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)

console_format = logging.Formatter("%(levelname)s | %(message)s")
file_format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This is DEBUG message for payment")
logger.info("This is INFO message for payment")
logger.warning("This is Warning message for payment")
logger.error("This is Error message for payment")

# For Customer

logger = logging.getLogger("app.customer")
logger.setLevel(logging.INFO)

customer_console_handler = logging.StreamHandler()
customer_console_handler.setLevel(logging.DEBUG)

customer_file_handler = logging.FileHandler("app.log")
customer_file_handler.setLevel(logging.INFO)

customer_console_format = logging.Formatter("%(levelname)s | %(message)s")
customer_file_format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

customer_console_handler.setFormatter(customer_console_format)
customer_file_handler.setFormatter(customer_file_format)

logger.addHandler(customer_console_handler)
logger.addHandler(customer_file_handler)

logger.debug("This is DEBUG message for customer")
logger.info("This is INFO message for customer")
logger.warning("This is Warning message for customer")
logger.error("This is Error message for customer")