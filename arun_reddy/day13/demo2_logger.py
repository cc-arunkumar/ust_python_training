import logging 


logger=logging.getLogger("app.paymnets")
logger.setLevel(logging.INFO)

console_handler=logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

file_handler=logging.FileHandler("app.payments.log")
file_handler.setLevel(logging.DEBUG)

console_format=logging.Formatter("%(levelname)s | %(message)s | %(lineno)d")
file_format=logging.Formatter("%(asctime)s | %(levelname)s | %(lineno)d")

file_handler.setFormatter(file_format)
console_handler.setFormatter(console_format)


logger.addHandler(file_handler)
logger.addHandler(console_handler)


#======================================================================================


logger1=logging.getLogger("app.customer")
logger1.setLevel(logging.DEBUG)

console_handler1=logging.StreamHandler()
console_handler1.setLevel(logging.DEBUG)

file_handler1=logging.FileHandler("app.customer.log")
file_handler1.setLevel(logging.WARNING)

file_handler1.setFormatter(file_format)
console_handler.setFormatter(console_format)


logger.addHandler(file_handler1)
logger.addHandler(console_handler1)


logger.debug("This is a DEBUG message (only file)")
logger.info("This is an INFO message")
logger.warning("This is an warning message")
logger.error("This is an error message")