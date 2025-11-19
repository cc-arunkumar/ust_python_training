import logging
logger=logging.getLogger("app.payment")
logger.setLevel(logging.DEBUG)

logger1=logging.getLogger("app.customer")
logger1.setLevel(logging.DEBUG)

console_handler=logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
file_handler=logging.FileHandler("handlng.log")
file_handler.setLevel(logging.INFO)

# console_formatter=logging.Formatter("%(name)s | %(lineno)d | %(message)s ")
# file_formatter=logging.Formatter("%(name)s | %(lineno)d | %(message)s ")

console_handler.setFormatter(logging.Formatter("%(name)s | %(lineno)d | %(message)s "))
file_handler.setFormatter(logging.Formatter("%(name)s | %(lineno)d | %(message)s "))

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger1.addHandler(console_handler)
logger1.addHandler(file_handler)

logger.debug("This is the message for payment DEBUG")
logger.info("This is the message for payment INFO")
logger.warning("This is the message for payment WARNING")

logger1.debug("This is the message for customer DEBUG")
logger1.info("This is the message for customer INFO")
logger1.warning("This is the message for customer WARNING")