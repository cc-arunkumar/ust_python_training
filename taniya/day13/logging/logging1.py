import logging
# create logger
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

# handlers(where logs go)
console_handler=logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# file
file_handler=logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

# formmating
console_format=logging.Formatter("%(levelname)s | %(message)s | line: %(lineno)d")
file_format=logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# attach ahndler to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This is a DEBUG message (only file)")
logger.info("This is an INFO message")
logger.error("This is an ERROR message")
logger.warning("This is a WARNING message")