import logging

#1.Create Logger
logger = logging.getLogger("customer")
logger.setLevel(logging.DEBUG)

#2.Handlers (where logs go)
#consols
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

#File
file_handler = logging.FileHandler("customer.log")
file_handler.setLevel(logging.DEBUG)

#3.Formatters (How to Look)
console_format = logging.Formatter("%(levelname)s | %(message)s | line: %(lineno)d")
file_format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s | %(name)s")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

#4.Attach handler to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

#5.Use the logger
logger.debug("This is a DEBUG message")
logger.info("This is a INFO message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
