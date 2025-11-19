import logging

# create logger 
logger = logging.getLogger("app.payment")
logger.setLevel(logging.DEBUG)

# console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# file handler
file_handler = logging.FileHandler("app_payment.log")
file_handler.setLevel(logging.DEBUG)

# formatters
console_format = logging.Formatter("%(levelname)s|%(message)s|%(lineno)d")
file_format = logging.Formatter("%(asctime)s|%(levelname)s|%(message)s")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# attach handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# use the logger
logger.debug("This is a debug message  for payment service(only file)")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")

print("Done! check app.log for payment service logs")
# customer service
logger = logging.getLogger("app.customer")
logger.setLevel(logging.INFO)

# console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# file handler
file_handler = logging.FileHandler("app_customer.log")
file_handler.setLevel(logging.DEBUG)

# formatters
console_format = logging.Formatter("%(levelname)s|%(message)s")
file_format = logging.Formatter("%(asctime)s|%(levelname)s|%(message)s")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# attach handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# use the logger
logger.debug("This is a debug message in customer service")
logger.info("This is an info message for customer")
logger.warning("This is a warning message in customer service")
logger.error("This is an error in customer service ")

print("Done! check app.log for customer service logs")