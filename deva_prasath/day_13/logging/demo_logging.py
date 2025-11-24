import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("Logger started")


logging.basicConfig(
    level=logging.DEBUG,
    format= "%(message)s| %(asctime)s | %(levelname)s | %(name)s | line: --> %(lineno)d | "
    )
logging.info("Info level")
logging.debug("Logger started")


payment_logger=logging.getLogger("payment_service")
customer_logger=logging.getLogger("customer_service")

payment_logger.info("Payment logger started")
customer_logger.info("Customer logger started")


# logging.basicConfig(level=logging.DEBUG,level=10)
# logging.info()
# logging.basicConfig(level=logging.INFO,level=20)
# logging.info("Actions Performed")

# logging.basicConfig(level=logging.WARN,level=30)
# logging.info("Something unexpected happen,might become a problem but program executes")


# logging.basicConfig(level=Warning,level=30)
# logging.info("low disk space")

# logging.basicConfig(level=Warning,level=40)
# logging.warn("a part of program failed")

# logging.error("failed to read file")
# # level 50- ---crirtical-program crashed
# #immediate action required since system is unusable
# #logger.critical("server down")

