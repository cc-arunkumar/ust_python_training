import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("logger started")
logging.basicConfig(
    level=logging.DEBUG,
    format=" %(message)s | %(asctime)s | %(levelname)s | %(name)s"
    )
logging.info("trying")
logging.debug("debugging")
payment_logger=logging.getLogger("payment.services")
customer_logger=logging.getLogger("customer.services")
payment_logger.info("payment service started")
customer_logger.info("customer service started")

