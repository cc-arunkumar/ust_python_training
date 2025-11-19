import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("logging started")

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(message)s | %(asctime)s | %(levelname)s | %(name)s | line: %(lineno)d"
)
logging.info("abc")
logging.debug("Debugger Working")

payment_logger = logging.getLogger("payment.services")
customer_logger = logging.getLogger("customer.services")

payment_logger.info("payment services started")
customer_logger.info("customer services started")