import logging

# 1 create logger 
logger = logging.getLogger("app_customer")
logger.setLevel(logging.DEBUG)

# 2 Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# 3 File 
file_handler = logging.FileHandler("new_app.log")
file_handler.setLevel(logging.INFO)

# Formatters
console_format = logging.Formatter("%(message)s | %(asctime)s | %(levelname)s | %(name)s | %(lineno)d")
file_format = logging.Formatter("%(message)s | %(levelname)s | %(name)s | %(lineno)d")

# Assign formatters correctly
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Test logs
logger.debug("this is debug message")
logger.info("this is Info message")
logger.warning("this is Warning message")
logger.error("this is error message")
logger.critical("this is Critical message")
