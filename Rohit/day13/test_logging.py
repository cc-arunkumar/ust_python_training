import logging   # Import Python's built-in logging module

# 1. Create logger
logger = logging.getLogger("app")   # Create a logger named "app"
logger.setLevel(logging.DEBUG)      # Set minimum logging level to DEBUG (captures all levels)

# 2. Console Handler
console_handler = logging.StreamHandler()   # Handler to output logs to console
console_handler.setLevel(logging.CRITICAL)  # Only CRITICAL logs will show in console

# 3. File Handler
file_handler = logging.FileHandler("app.log")   # Handler to write logs to file "app.log"
file_handler.setLevel(logging.INFO)             # Logs of INFO and above will be written to file

# 4. Formatters
console_format = logging.Formatter(
    "%(message)s | %(asctime)s | %(levelname)s | %(name)s | %(lineno)d"
)
file_format = logging.Formatter(
    "%(message)s | %(levelname)s | %(name)s | %(lineno)d"
)

# Assign formatters to handlers
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# 5. Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 6. Test logs
logger.debug("this is debug message")       # DEBUG → written to file only (not console)
logger.info("this is Info message")         # INFO → written to file only
logger.warning("this is Warning message")   # WARNING → written to file only
logger.error("this is error message")       # ERROR → written to file only
logger.critical("this is Critical message") # CRITICAL → written to file AND console
