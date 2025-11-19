import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("logging started")
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s | %(asctime)s  | %(levelname)s | %(name)s | line:%(lineno)d  "
    
)
logging.debug("debugger working")
logging.info("logging started")
payment_logger = logging.getLogger("payment.services")
customer_logger = logging.getLogger("Customer.services")
payment_logger.info("payment services started")
customer_logger.info("customer services started")
