import logging

# logging.basicConfig(level=logging.INFO)
# logging.info("Logger started...")

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s | %(asctime)s | %(levelname)s | %(name)s | line: %(lineno)d "
)
logging.info("message")
logging.debug("Working")

payment_logger = logging.getLogger("payment.services")
customer_logger = logging.getLogger("customer.services")
payment_logger.info("payment services started")
customer_logger.info("suatomer services started")

# debug - 10 - trace variable values or program flow 
# connecting to db
# info - 20 - show progress or actions performed 
# user logged in.
# warning - 30 - something unexpected happened might become a problem but program executes.
# low disk space.
# error - 40 - a serious issue occured and a part of program failed.
# program continue running, a specific part failed.
# failed to read the file.
# critial - 50 - program crashed (about to crash.) extremly serious 
# immediate action required since system is unuseable.
# server down - logger. critical


