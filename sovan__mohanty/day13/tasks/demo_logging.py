import logging

# logging.basicConfig(level=logging.INFO)
# logging.info("Logger Started")
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s | %(levelname)s | %(message)s | line: %(lineno)d | %(name)s"
                    )
logging.debug("Debugging is working")

payment_logger=logging.getLogger("payment.services")
customer_logger=logging.getLogger("customer.services")
payment_logger.info("Payment services started")
customer_logger.info("Customer services started")
