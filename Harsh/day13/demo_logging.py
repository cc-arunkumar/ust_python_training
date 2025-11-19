import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("Logger started ")
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s | %(asctime)s | %(levelname)s | %(name)s | line:-> %(lineno)d  "
)
logging.debug("debugger working")
logging.info("Logger started ")

pay_log=logging.getLogger("payment.services")
cust_log=logging.getLogger("customer.services")
pay_log.info("payment services started")
cust_log.info("customer services started")