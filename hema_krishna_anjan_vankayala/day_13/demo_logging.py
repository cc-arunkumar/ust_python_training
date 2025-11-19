import logging 
# logging.basicConfig(level=logging.INFO)
# logging.info("Logger Started")


# logging.basicConfig(level=logging.DEBUG,format="%(asctime)s | %(name)s | line -> %(lineno)d | %(message)s")
# logging.info("Info Level")
# logging.debug("Debugging")

#2025-11-19 10:00:10,511 | root | line -> 9 | Info Level
# 2025-11-19 10:00:10,512 | root | line -> 10 | Debugging

payment_logger = logging.getLogger("Payment service")
customer_logger = logging.getLogger("customer service")

payment_logger.info("payment services started")
customer_logger.info("customer services started")

# 2025-11-19 10:00:10,512 | Payment service | line -> 15 | payment services started
# 2025-11-19 10:00:10,512 | customer service | line -> 16 | customer services started