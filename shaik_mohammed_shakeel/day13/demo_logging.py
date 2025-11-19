import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("Logging started")

logging.basicConfig(
    level=logging.DEBUG,
    format=" %(asctime)s | %(levelname)s | %(name)s | line: %(lineno)d | %(message)s"
    )
logging.info("started")

logging.debug("Debugger started working !")



payment_logger = logging.getLogger("payment services")
customer_logger = logging.getLogger("customer services")
payment_logger.info("started")
customer_logger.info("yes")