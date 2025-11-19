import logging

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

payment_logger = logging.getLogger("app.payment")
payment_logger.setLevel(logging.ERROR)

customer_logger = logging.getLogger("app.customer")
customer_logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)

console_formatter = logging.Formatter("%(levelname)s | %(message)s | line: %(lineno)d | %(name)s")
file_formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s | %(name)s")

console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# logger.addHandler(console_handler)
# logger.addHandler(file_handler)
customer_logger.addHandler(console_handler)
customer_logger.addHandler(file_handler)

payment_logger.addHandler(console_handler)
payment_logger.addHandler(file_handler)

customer_logger.debug("Debug is running")
customer_logger.info("Info is running")
customer_logger.warning("Warning is running")
payment_logger.error("Error is running")
payment_logger.critical("Critical is running")
