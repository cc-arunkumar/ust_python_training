import logging  # Import the logging module

# Create a logger named "app"
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)  # Set the logging level to DEBUG to capture all levels of logs

# Create a console handler to output logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Set console handler to capture DEBUG and above

# Create a file handler to write logs to a file named "app.log"
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)  # Set file handler to capture DEBUG and above

# Define the format for console logs: includes level, message, and line number
console_format = logging.Formatter("%(levelname)s | %(message)s|line:%(lineno)d")

# Define the format for file logs: includes message twice and level
file_format = logging.Formatter("%(message)s|%(levelname)s | %(message)s|")

# Apply the formatters to the respective handlers
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add both handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Log messages of various severity levels
logger.debug("this is a debug message (only on file)")  # DEBUG message
logger.info("this is a info message")                   # INFO message
logger.warning("this is a warning message")             # WARNING message
logger.error("this is a error message")                 # ERROR message
logger.critical("this is a critical message")           # CRITICAL message

# Final print statement to indicate completion
print("Done! check app.log for full logs")