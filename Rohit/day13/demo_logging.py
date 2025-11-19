import logging

# logging.basicConfig(level=logging.INFO)
# logging.info("This is an info message")

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s |%(asctime)s | %(levelname)s | %(name)s | %(lineno)d  "
    
)

logging.debug("This is a debug message")
logging.info("This is an info message")
# stream logger
p_logger = logging.getLogger("payment.services")
c_logger = logging.getLogger("customer.services")

p_logger.info("Payment service started")
c_logger.info("Customer service started")

# debug -10 trace variable valuse or program file(connecting to db)
# info 20 to show progress or actions performed (user logged in)
# waring 30 something unexpected happen might become a problem but pogram executes or continue to executes (low disk space)
# error - 40 a serious issue occured a part of program failed 
# program continue running , a specific part failed .(failed to read file)
# Critical 50 program crashed (about to crash) extrememly serious 
# immediate action required since system is unusable(server down) 

