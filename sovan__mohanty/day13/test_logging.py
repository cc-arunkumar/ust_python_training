import logging

# #1. Create logger
# logger=logging.getLogger("app")
# logger.setLevel(logging.DEBUG) #master level

# #2. Handlers(where logs go)
# #Console
# console_handler=logging.StreamHandler()
# console_handler.setLevel(logging.INFO)

# #File
# file_handler=logging.FileHandler("app.log")
# file_handler.setLevel(logging.DEBUG)

# #3. Formatter(How logs look)
# console_formatter=logging.Formatter("%(levelname)s | %(message)s | line: %(lineno)d")
# file_format=logging.Formatter("%(asctime)s | %(levelname)s| %(message)s")

# console_handler.setFormatter(console_formatter)
# file_handler.setFormatter(file_format)

# #4. Attach handlers to logger
# logger.addHandler(console_handler)
# logger.addHandler(file_handler)

# logger.debug("This a DEBUG message")
# logger.info("This is an INFO message")
# logger.warning("This is a WARNING message")
# logger.error("This is an ERROR message")

# print("Done! Check app.log")

logger=logging.getLogger("app_customer")
logger.setLevel(logging.DEBUG) 

file_handler=logging.FileHandler("app_Customer.log")
file_handler.setLevel(logging.DEBUG)

console_handler=logging.StreamHandler()
console_handler.setLevel(logging.INFO)

console_formatter=logging.Formatter("%(levelname)s | %(message)s | line: %(lineno)d")
file_formatter=logging.Formatter("%(asctime)s | %(levelname)s| %(message)s")

console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This is a DEBUG file")
logger.info("This is an INFO file")
logger.warning("This is a WARNING file")
logger.error("This is an ERROR file")
logger.critical("This is a CRITICAL file")

print("Done! check app_customer log file")