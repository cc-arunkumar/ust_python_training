import logging

# logging.basicConfig(level=logging.INFO)
# logging.info("This is an info message")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s | line: %(lineno)d | %(message)s"
)
# logging.info("This is a message")
# logging.debug("This is a message")

payment_logger=logging.getLogger("payment.servers")
customer_logger=logging.getLogger("customer.server")
payment_logger.info("payment service start")
customer_logger.info("customer service start")


