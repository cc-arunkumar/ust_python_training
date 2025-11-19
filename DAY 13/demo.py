import logging

# logging.basicConfig(level=logging.INFO)
# logging.info("Logger Started")
# logging.basicConfig(
#     level=logging.INFO
# )
# logging.debug("Working")


logging.basicConfig(
    # level=logging.INFO
    level=logging.DEBUG,
    format="| %(message)s | %(asctime)s | %(levelname)s | %(name)s | line -> %(lineno)d "
)

logging.debug("Debugger Working")



payment_logger=logging.getLogger("payment.services")
customer_logger=logging.getLogger("customer.services")

payment_logger.info("Payment Services Started")
customer_logger.info("Customer Services Started")

