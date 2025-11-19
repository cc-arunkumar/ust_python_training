import logging

#1. Create logger
logger = logging.getLogger("app.payment")
logger.setLevel(logging.DEBUG)

logger=logging.getLogger("app.customer")
logger.setLevel(logging.INFO)

# 2. Handlers (Where logs go)
# Console
console_handler=logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# File
file_handler=logging.FileHandler("app_test.log")
file_handler.setLevel(logging.DEBUG)

# 3. Formatters (How logs look)
console_format=logging.Formatter("%(levelname)s | %(message)s | line: %(lineno)d")
file_format=logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# 4. Attach handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 5. Use the logger
logger.debug("This is a DEBUG message(only file)")
logger.info("This is a INFO message")
logger.warning("This is a WARNING message")
logger.error("This is a ERROR message")

print("Done! check app.log for full logs")