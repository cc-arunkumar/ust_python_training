import logging

# 1.Create logger
logger1 = logging.getLogger("app.payment") #app.payment
logger1.setLevel(logging.DEBUG)

logger = logging.getLogger("app.customer")  #app.customer
logger.setLevel(logging.INFO)

# 2.Handlers(where logs go)
# console

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# file
file_handler = logging.FileHandler("app_test.log")
file_handler.setLevel(logging.DEBUG)

# 3.Formatters(How logs look)
console_format = logging.Formatter("%(levelname)s | %(message)s | line: %(lineno)d")
file_format = logging.Formatter("%(asctime)s | %(levelno)d | %(message)s")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# 4.Attach handlers to logger
logger1.addHandler(console_handler)
logger1.addHandler(file_handler)
logger.addHandler(file_handler)
logger.addHandler(file_handler)

# 5.Use the logger

logger.debug("This is a DUBUG message")
logger1.debug("This is a DUBUG message")
logger.debug("This is a DUBUG message")
logger1.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger1.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")


print("Done! Check app_test.log for full logs")

