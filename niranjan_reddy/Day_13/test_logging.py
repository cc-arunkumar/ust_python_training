import logging

# Create a logger object named "app"
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)  # Set minimum log level to DEBUG

# --------------------------
# Handlers (where logs go)
# --------------------------

# Handler for console output
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Logs at DEBUG and above

# Handler for writing logs to a file
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

# --------------------------
# Formatters (log message structure)
# --------------------------

# Formatter for console logs
console_formatter = logging.Formatter("%(asctime)s | %(message)s | %(levelname)s")

# Formatter for file logs (includes more diagnostic info)
file_formatter = logging.Formatter("%(asctime)s | %(name)s | Line -> %(lineno)d")

# Apply formatters to handlers
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# --------------------------
# Example log messages
# --------------------------

logger.debug("DEBUG: trace variable values or program execution.")
logger.info("INFO: show progress or actions performed.")
logger.warning("WARNING: unexpected event; might become an issue but program continues.")
logger.error("ERROR: serious issue occurred; part of the program failed.")
logger.critical("CRITICAL: program crashed or is about to crash; extremely serious.")
