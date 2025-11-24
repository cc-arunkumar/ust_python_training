import logging

# logging.basicConfig(level=logging.DEBUG)

# # logging.info("process started")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | line -> %(lineno)d | %(message)s"
)
# logging.info("info working")
# #2025-11-19 10:29:47,274 | INFO | root | line -> 12 | info working
# logging.debug("debugger working")
#2025-11-19 10:23:56,157 | DEBUG | root | line -> 12 | debugger working

payment_logger=logging.getLogger("Payment service")
customer_logger=logging.getLogger("customer service")

payment_logger.info("payment services started")
#2025-11-19 10:36:33,620 | INFO | Payment service | line -> 19 | payment services started
customer_logger.info("customer services started")
#2025-11-19 10:36:33,621 | INFO | customer service | line -> 20 | customer services started
payment_logger.debug("debugging")
payment_logger.warning("warning")
payment_logger.error("error")
payment_logger.critical("critical")