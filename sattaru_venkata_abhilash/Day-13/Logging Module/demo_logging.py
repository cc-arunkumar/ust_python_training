import logging

# Basic logging configuration to log messages at the INFO level
logging.basicConfig(level=logging.INFO)
logging.info("Logging started")  # Log a basic info message indicating that logging has started

# More advanced logging configuration with additional details like timestamp, log level, logger name, and line number
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s  | %(asctime)s | %(levelname)s | %(name)s | line->%(lineno)d"  # Customize the log format
)
logging.info("Login info")  # Log an info message indicating login information
logging.debug("Logging debug working")  # This is a debug message that will not show up unless the level is set to DEBUG

# Creating custom loggers for specific services
payment_logger = logging.getLogger("payment.services")  # Logger specifically for payment-related services
customer_logger = logging.getLogger("customer.services")  # Logger specifically for customer-related services

# Log messages specific to payment and customer services
payment_logger.info("Payment services started")  # Log the info message that payment services started
customer_logger.info("Customer services started")  # Log the info message that customer services started

# Logging Levels Overview:
#  LEVEL 10 — DEBUG
# Purpose:
# - Trace variable values
# - Trace program execution flow
# - Internal developer-level details (for debugging)
# - Connecting to database, loading configurations, etc.

# Example:
# - Connecting to DB…
# - x value = 42
# - Function process_data() entered

#  LEVEL 20 — INFO
# Purpose:
# - Show progress
# - Show actions being performed
# - Normal behavior of the application (end users would see these messages)
# Example:
# - User logged in
# - File uploaded successfully
# - Processing completed

#  LEVEL 30 — WARNING
# Purpose:
# - Something unexpected happened but the program can still run
# - Might become a problem later, indicates a potential issue
# Example:
# - Low disk space
# - API response delayed
# - Logger warning: Retrying connection

#  LEVEL 40 — ERROR
# Purpose:
# - A serious issue occurred, a part of the program failed
# - The program continues to run, but a specific task is broken
# Example:
# - Failed to read file
# - Database write failed
# - Payment service timeout

#  LEVEL 50 — CRITICAL
# Purpose:
# - Extremely serious failure, program crashed or about to crash
# - Immediate attention is required, system becomes unusable
# Example:
# - Server down
# - Critical system failure
# - Memory corruption detected
