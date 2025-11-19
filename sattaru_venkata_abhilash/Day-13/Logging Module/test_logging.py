import logging

# ---------------------------------------------------
# 1. Create a Logger Object
# ---------------------------------------------------
# 'app' is the logger name.
# logger.setLevel(DEBUG) → Master/logging level for this logger.
# This means: logger will ACCEPT all levels ≥ DEBUG.
logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)


# ---------------------------------------------------
# 2. Create Handlers (Output Targets)
# ---------------------------------------------------
# Handler 1: Console
# This sends log messages to the terminal (stdout)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  
# Console will show everything from DEBUG → CRITICAL

# Handler 2: File
# This writes logs to a file named 'app.log'
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
# File will store only: INFO, WARNING, ERROR, CRITICAL


# ---------------------------------------------------
# 3. Create Formatters (How log messages look)
# ---------------------------------------------------
# Console format:
#   app_name | timestamp | level | line number
console_formater = logging.Formatter(
    "%(name)s | %(asctime)s | %(levelname)s | line: %(lineno)d"
)

# File format:
#   LEVEL | message | level number
file_formater = logging.Formatter(
    "%(levelname)s | %(message)s | %(levelno)d"
)


# ---------------------------------------------------
# 4. Attach the Formatters to Handlers
# ---------------------------------------------------
console_handler.setFormatter(console_formater)
file_handler.setFormatter(file_formater)


# ---------------------------------------------------
# 5. Add Handlers to Logger
# ---------------------------------------------------
# Now logger will output logs to both console and file
logger.addHandler(console_handler)
logger.addHandler(file_handler)


# ---------------------------------------------------
# 6. Test Logging with All Levels (Clean & Professional)
# ---------------------------------------------------

logger.debug("DEBUG: Tracking program flow and variable values")
logger.info("INFO: Application started successfully")
logger.warning("WARNING: Low disk space detected")
logger.error("ERROR: Failed to read the required file")
logger.critical("CRITICAL: System failure — immediate attention required")

print("Done! Check app.log for logs.")


# sample output:
# app | 2025-11-19 12:45:10,455 | DEBUG | line: 46
# app | 2025-11-19 12:45:10,456 | INFO | line: 47
# app | 2025-11-19 12:45:10,456 | WARNING | line: 48
# app | 2025-11-19 12:45:10,456 | ERROR | line: 49
# app | 2025-11-19 12:45:10,456 | CRITICAL | line: 50
# Done! Check app.log for logs.
