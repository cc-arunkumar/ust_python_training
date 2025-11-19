import logging
# logging.basicConfig(level=logging.INFO)

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s%(asctime)s - %(levelname)s - %(name)s - ----> %(lineno)d - "

)
logging.info("logger started")
logging.debug("debugger working")
payment_logger=logging.getLogger("payment.services")
customer_logger=logging.getLogger("customer.services")
payment_logger.info("payment services started")
customer_logger.info("customer services started")