import logging

# -----------------------------
# Logger Setup
# -----------------------------
# Create a logger named "app".
# DEBUG level ensures all messages (debug → critical) are captured.
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

# -----------------------------
# Console Handler
# -----------------------------
# StreamHandler sends logs to console (stdout).
# Only WARNING and above will be shown on console.
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# -----------------------------
# File Handler
# -----------------------------
# FileHandler writes logs to 'app.log'.
# DEBUG and above will be written to file.
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# -----------------------------
# Formatters
# -----------------------------
# Console formatter: simple level + message
console_formatter = logging.Formatter("%(levelname)s | %(message)s")

# File formatter: detailed with timestamp, level, logger name, and message
file_formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

# Attach formatters to handlers
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# -----------------------------
# Attach Handlers to Logger
# -----------------------------
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# -----------------------------
# Logging Demonstration
# -----------------------------
logger.debug("Debugging")
logger.info("Information")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")

# -----------------------------
# Sample Outputs
# -----------------------------

# Console Output:
# WARNING | Warning
# ERROR | Error
# CRITICAL | Critical

# File Output (app.log):
# 2025-11-24 09:38:00,123 | DEBUG | app | Debugging
# 2025-11-24 09:38:00,124 | INFO | app | Information
# 2025-11-24 09:38:00,125 | WARNING | app | Warning
# 2025-11-24 09:38:00,126 | ERROR | app | Error
# 2025-11-24 09:38:00,127 | CRITICAL | app | Critical
