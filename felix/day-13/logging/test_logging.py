import logging

# ---------------------------------------------------------
# Logger configuration for Payment module
# ---------------------------------------------------------

# Create a logger instance for payment-related logs
logger = logging.getLogger("app.payment")
logger.setLevel(logging.DEBUG)   # Allow all levels (DEBUG → ERROR)

# Create and configure a console handler (prints logs to terminal)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Show all logs on console

# Create and configure a file handler (writes logs to app.log)
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)  # Write only INFO and above to file

# Define log message formats
console_format = logging.Formatter("%(levelname)s | %(message)s")
file_format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

# Apply formats to handlers
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Attach handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Write sample log messages for Payment
logger.debug("This is DEBUG message for payment")
logger.info("This is INFO message for payment")
logger.warning("This is Warning message for payment")
logger.error("This is Error message for payment")

# ---------------------------------------------------------
# Logger configuration for Customer module
# ---------------------------------------------------------

# Create a separate logger for customer-related logs
logger = logging.getLogger("app.customer")
logger.setLevel(logging.INFO)  # Only INFO and above will be processed

# Console handler for customer logs
customer_console_handler = logging.StreamHandler()
customer_console_handler.setLevel(logging.DEBUG)  # Console shows all logs

# File handler for customer logs (writes to same file: app.log)
customer_file_handler = logging.FileHandler("app.log")
customer_file_handler.setLevel(logging.INFO)  # Only INFO and above stored

# Define formats for customer log output
customer_console_format = logging.Formatter("%(levelname)s | %(message)s")
customer_file_format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

# Apply formatting
customer_console_handler.setFormatter(customer_console_format)
customer_file_handler.setFormatter(customer_file_format)

# Attach handlers to customer logger
logger.addHandler(customer_console_handler)
logger.addHandler(customer_file_handler)

# Write sample log messages for Customer
logger.debug("This is DEBUG message for customer")  # Will not appear (level < INFO)
logger.info("This is INFO message for customer")
logger.warning("This is Warning message for customer")
logger.error("This is Error message for customer")


# sample output

# DEBUG | This is DEBUG message for payment
# INFO | This is INFO message for payment
# WARNING | This is Warning message for payment
# ERROR | This is Error message for payment
# INFO | This is INFO message for customer
# WARNING | This is Warning message for customer
# ERROR | This is Error message for customer

