import logging

# logging.basicConfig(level=logging.INFO)
# logging.info("Logger activated")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s | %(asctime)s | %(levelname)s | %(name)s | Lineno : %(lineno)d"
)
logging.info("Trying")
logging.debug("Debugger Working")
# logging.error("error")

payment_logger = logging.getLogger("payment.services")
customer_logger = logging.getLogger("customer.services")

payment_logger.info("Payment Services Started")
customer_logger.info("Customer Services Started")