import logging

logger=logging.getLogger("app")
logger.setLevel(logging.DEBUG)


# logging.getLogger("app"): This creates a logger with the name "app".
# You can think of the logger as a tool that you use to send logging message

# logger.setLevel(logging.DEBUG): This sets the threshold level of the logger to DEBUG,
# which means the logger will capture messages of level DEBUG and above.


console_handler=logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)


file_handler=logging.FileHandler("app.log")
file_handler.setLevel(logging.WARNING)

console_format=logging.Formatter("%(levelname)s | %(message)s |line:%(lineno)d |%(name)s")
file_format=logging.Formatter("%(asctime)s | %(levelname)s |%(message)s |%(name)s")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)


logger.addHandler(console_handler)
logger.addHandler(file_handler)


logger.debug("This is a DEBUG message(only file)")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")

print("Done")

