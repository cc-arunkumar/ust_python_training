import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | line: %(lineno)d | %(message)s"
)
logging.info("logging")
logging.debug("Debugger Working")

payment_logger = logging.getLogger("payment.services")
customer_logger = logging.getLogger("customer.services")

payment_logger.info("Payment Services Started")
customer_logger.info("Customer Services Started")