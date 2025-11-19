import logging
logger=logging.getLogger('app')
logger.setLevel(logging.ERROR)

console_handler=logging.StreamHandler()
console_handler.setLevel(logging.INFO)
file_handler=logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

console_formatter=logging.Formatter("%(message)s | %(asctime)s | %(name)s | %(lineno)d")
file_formatter=logging.Formatter("%(message)s | %(asctime)s | %(name)s | %(lineno)d")

console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This is a DEBUG message")
logger.info("This is a INFO message")
logger.warning("This is a WARNING message")
logger.error("This is a ERROR message")
print("done app cheak")