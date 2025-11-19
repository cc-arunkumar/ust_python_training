import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("Logger started")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s | line: %(lineno)d | %(message)s"
)

logging.info("logger started")
logging.debug("debugger started")

# stream logger
payment_logger = logging.getLogger("payment.services")
customer_logger = logging.getLogger("customer.services")
employment_logger = logging.getLogger("employee.services")
payment_logger.info("payment services started")
customer_logger.info("customer services started")
employment_logger.info("Employment services started")

# Sample output
# 2025-11-19 11:09:31,941 | INFO | root | line: 10 | logger started
# 2025-11-19 11:09:31,941 | DEBUG | root | line: 11 | debugger started
# 2025-11-19 11:09:31,941 | INFO | payment.services | line: 17 | payment services started
# 2025-11-19 11:09:31,941 | INFO | customer.services | line: 18 | customer services started
# 2025-11-19 11:09:31,941 | INFO | employee.services | line: 19 | Employment services started


