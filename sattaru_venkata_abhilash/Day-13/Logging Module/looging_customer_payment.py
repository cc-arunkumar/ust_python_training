import logging

# ---------------------------------------------------
# LOGGER 1: payment logger
# ---------------------------------------------------
payment_logger = logging.getLogger("app.payment")
payment_logger.setLevel(logging.WARNING)

payment_file_handler = logging.FileHandler("app_payment.log")
payment_file_handler.setLevel(logging.WARNING)

payment_formatter = logging.Formatter(
    "%(levelname)s | %(message)s | %(levelno)d"
)
payment_file_handler.setFormatter(payment_formatter)

payment_logger.addHandler(payment_file_handler)


# ---------------------------------------------------
# LOGGER 2: customer logger
# ---------------------------------------------------
customer_logger = logging.getLogger("app.customer")
customer_logger.setLevel(logging.DEBUG)

customer_file_handler = logging.FileHandler("app_customer.log")
customer_file_handler.setLevel(logging.INFO)

customer_formatter = logging.Formatter(
    "%(levelname)s | %(message)s | %(levelno)d"
)
customer_file_handler.setFormatter(customer_formatter)

customer_logger.addHandler(customer_file_handler)


# ---------------------------------------------------
# Optional: Console Handler shared by both loggers
# ---------------------------------------------------
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter(
    "%(name)s | %(asctime)s | %(levelname)s | line: %(lineno)d"
)
console_handler.setFormatter(console_formatter)

payment_logger.addHandler(console_handler)
customer_logger.addHandler(console_handler)


# ---------------------------------------------------
# TEST LOGGING
# ---------------------------------------------------

# These logs go to app_payment.log (WARNING + ERROR + CRITICAL)
payment_logger.debug("Payment Debug")
payment_logger.info("Payment Info")
payment_logger.warning("Payment Warning")
payment_logger.error("Payment Error")
payment_logger.critical("Payment Critical")

# These logs go to app_customer.log (INFO + WARNING + ERROR + CRITICAL)
customer_logger.debug("Customer Debug")
customer_logger.info("Customer Info")
customer_logger.warning("Customer Warning")
customer_logger.error("Customer Error")
customer_logger.critical("Customer Critical")

print("Done! Check app_payment.log and app_customer.log")



# sample output:

# payment

# app.payment | 2025-11-19 13:00:12,450 | DEBUG | line: 52
# app.payment | 2025-11-19 13:00:12,450 | INFO | line: 53
# app.payment | 2025-11-19 13:00:12,450 | WARNING | line: 54
# app.payment | 2025-11-19 13:00:12,450 | ERROR | line: 55
# app.payment | 2025-11-19 13:00:12,450 | CRITICAL | line: 56

# customer

# app.customer | 2025-11-19 13:00:12,451 | DEBUG | line: 60
# app.customer | 2025-11-19 13:00:12,451 | INFO | line: 61
# app.customer | 2025-11-19 13:00:12,451 | WARNING | line: 62
# app.customer | 2025-11-19 13:00:12,451 | ERROR | line: 63
# app.customer | 2025-11-19 13:00:12,451 | CRITICAL | line: 64

# Done! Check app_payment.log and app_customer.log
