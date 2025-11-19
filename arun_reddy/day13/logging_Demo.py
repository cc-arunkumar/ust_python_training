import logging 

logger=logging.getLogger("app")
logger.setLevel(logging.DEBUG) # master level

console_handler=logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler=logging.FileHandler("app.log")
file_handler.setLevel(logging.WARNING)

console_format=logging.Formatter(" %(levelname)s | %(message)s | line: %(lineno)d")
file_format=logging.Formatter(" %(asctime)s |%(levelname)s | %(message)s")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This is a DEBUG message (only file)")
logger.info("This is an INFO message")
logger.warning("This is an warning message")
logger.error("This is an error message")

print("!Done Check app.log for full logs")