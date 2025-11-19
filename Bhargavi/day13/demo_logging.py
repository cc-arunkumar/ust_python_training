
# logging.basicConfig(level=logging.INFO)
# logging.info("logging status")

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format=" %(asctime)s | %(levelname)s | %(name)s | line: %(lineno)d | %(message)s"
)
logging.debug("This is a debug message")
logging.info("This is an info message")

payment_logger = logging.getLogger("payment.services")
customer_logger = logging.getLogger("customer.services")
payment_logger.info("payment")
customer_logger.info("info")

#output
# 2025-11-19 09:27:07,419 | DEBUG | root | line: 12 | This is a debug message
#  2025-11-19 09:27:07,419 | INFO | root | line: 13 | This is an info message
#  2025-11-19 09:27:07,420 | INFO | payment.services | line: 17 | payment
#  2025-11-19 09:27:07,421 | INFO | customer.services | line: 18 | info

