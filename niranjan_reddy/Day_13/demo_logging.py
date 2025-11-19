import logging
# logging.basicConfig(level=logging.INFO)

# logging.info("Logging Started")
logging.basicConfig(
    level=logging.DEBUG,
    format=" %(message)s | %(asctime)s | %(levelname)s | %(name)s | line-> %(lineno)d "
)

logging.info("logger info")
logging.debug("logging debug working")

#  logger info | 2025-11-19 10:39:29,587 | INFO | root | line-> 10 
#  logging debug working | 2025-11-19 10:39:29,587 | DEBUG | root | line-> 11 

payment_logger=logging.getLogger("payment.services")
customer_logger=logging.getLogger("customer.services")

payment_logger.info("payment services started")
customer_logger.info("customer services started")

# 2025-11-19 10:35:52,673 | INFO | payment.services | line-> 16 | payment services started
# 2025-11-19 10:35:52,673 | INFO | customer.services | line-> 17 | customer services started