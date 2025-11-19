import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("Logging started")
logging.basicConfig(
    level=logging.INFO, format="%(message)s %(asctime)s | %(levelname)s | %(name)s | line: %(lineno)d | "
)
logging.info("info level")
logging.debug("debug started")

paymentlogger=logging.getLogger("payment.services")
customerlogger=logging.getLogger("customer.services")
paymentlogger.info("payment services started")
customerlogger.info("customer services started")