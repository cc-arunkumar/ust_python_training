import logging

# -----------------------------
# Logger: Payment
# -----------------------------
# Create a logger for payment-related events.
# DEBUG level ensures all messages (debug → critical) are captured.
logger_payment = logging.getLogger("app.payment")
logger_payment.setLevel(logging.DEBUG)

# Console handler for payment logger
# Only WARNING and above will be shown on console.
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# File handler for payment logger
# DEBUG and above will be written to 'app_payment.log'.
file_handler = logging.FileHandler('app_payment.log')
file_handler.setLevel(logging.DEBUG)

# Formatters for console and file
console_formatter = logging.Formatter("%(levelname)s | %(message)s")
file_formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# Attach handlers to payment logger
logger_payment.addHandler(file_handler)
logger_payment.addHandler(console_handler)


# -----------------------------
# Logger: Customer
# -----------------------------
# Create a logger for customer-related events.
# WARNING level ensures only warnings and above are processed.
logger_customer = logging.getLogger("app_customer")
logger_customer.setLevel(logging.WARNING)

# Console handler for customer logger
console_handler_customer = logging.StreamHandler()
console_handler_customer.setLevel(logging.WARNING)

# File handler for customer logger
file_handler_customer = logging.FileHandler('app_customer.log')
file_handler_customer.setLevel(logging.DEBUG)

# Formatters for customer logger
console_formatter_customer = logging.Formatter("%(levelname)s | %(message)s")
file_formatter_customer = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

console_handler_customer.setFormatter(console_formatter_customer)
file_handler_customer.setFormatter(file_formatter_customer)

# Attach handlers to customer logger
logger_customer.addHandler(file_handler_customer)
logger_customer.addHandler(console_handler_customer)


# -----------------------------
# Logging Demonstration
# -----------------------------
logger_payment.debug("Debugging")
logger_payment.info("Information")
logger_payment.warning("Warning")
logger_payment.error("Error")
logger_payment.critical("Critical")

print("=====================")

logger_customer.debug("Debugging")
logger_customer.info("Information")
logger_customer.warning("Warning")
logger_customer.error("Error")
logger_customer.critical("Critical")


# -----------------------------
# Sample Outputs
# -----------------------------

# Console Output (payment logger):
# WARNING | Warning
# ERROR | Error
# CRITICAL | Critical

# Console Output (customer logger):
# =====================
# WARNING | Warning
# ERROR | Error
# CRITICAL | Critical

# File Output (app_payment.log):
# 2025-11-24 09:38:00,123 | DEBUG | app.payment | Debugging
# 2025-11-24 09:38:00,124 | INFO | app.payment | Information
# 2025-11-24 09:38:00,125 | WARNING | app.payment | Warning
# 2025-11-24 09:38:00,126 | ERROR | app.payment | Error
# 2025-11-24 09:38:00,127 | CRITICAL | app.payment | Critical

# File Output (app_customer.log):
# 2025-11-24 09:38:00,128 | WARNING | app_customer | Warning
# 2025-11-24 09:38:00,129 | ERROR | app_customer | Error
# 2025-11-24 09:38:00,130 | CRITICAL | app_customer | Critical
