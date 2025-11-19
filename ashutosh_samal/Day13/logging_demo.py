import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("Logging started")

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s | %(levelname)s | %(name)s | line: %(lineno)d | %(message)s "
    )
logging.debug("Logger started")

payment_logger = logging.getLogger("Payment Services")
customer_logger = logging.getLogger("Customer Services")
payment_logger.info("Payment logger started")
customer_logger.info("Customer logger started")