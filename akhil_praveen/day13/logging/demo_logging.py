import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("Logger started")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | line: %(lineno)d | %(message)s"
)

logging.info("Logger started")
logging.debug("Debugger working")

payment_logger = logging.getLogger("payment.services")
customer_logger = logging.getLogger("customer.services")
payment_logger.info("payment.services started")
customer_logger.info("customer.services started")