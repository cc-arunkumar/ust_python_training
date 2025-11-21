import logging

payment_logger=logging.getLogger("app_payment")
customer_logger=logging.getLogger("app_customer")

payment_logger.setLevel(logging.CRITICAL)
customer_logger.setLevel(logging.WARNING)

# Adding handlers
payment_handler=logging.FileHandler("payment_log.log")
payment_handler.setLevel(logging.INFO)

customer_handler=logging.StreamHandler()
customer_handler.setLevel(logging.WA)



#Formatting
payment_format=logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
payment_handler.setFormatter(payment_format)


#Connecting handler to logger
payment_logger.addHandler(payment_handler)



payment_logger.debug("This is a DEBUG message")
payment_logger.info("This is a INFO message")
payment_logger.warning("This is a WARNING message")
payment_logger.error("This is a ERROR message")
payment_logger.critical("This is a CRITICAL message")


