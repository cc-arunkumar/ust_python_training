import logging

# Creating logger
logger=logging.getLogger("app")
logger.setLevel(logging.DEBUG) #for the enitire application

# 2. Handlers (where to go)
#Console
console_handler=logging.StreamHandler()
console_handler.setLevel(logging.INFO)

#for file
file_handler=logging.FileHandler("app.log")
file_handler.setLevel(logging.WARNING)

# 3. Formatter (How to log - format)

console_format=logging.Formatter("%(levelname)s | %(message)s | line -> %(lineno)d")
file_format=logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

#4. Conecting Handler to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


#5. USing logger
logger.debug("This is a DEBUG message")
logger.info("This is a INFO message")
logger.warning("This is a WARNING message")
logger.error("This is a ERROR message")
logger.critical("This is a CRITICAL message")


print("Completed")