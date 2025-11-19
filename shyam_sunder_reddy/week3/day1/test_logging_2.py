import logging

#Logger_payment
logger_payment=logging.getLogger("app.payment")
logger_payment.setLevel(logging.DEBUG)

#logger_customer
logger_customer=logging.getLogger("app_customer")
logger_customer.setLevel(logging.WARNING)

#logger payment
console_handler=logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

file_handler=logging.FileHandler('app_payment.log')
file_handler.setLevel(logging.DEBUG)

console_formater=logging.Formatter("%(levelname)s | %(message)s")
file_formater=logging.Formatter("%(asctime)s | %(levelname)s | %(name)s |%(message)s")

console_handler.setFormatter(console_formater)
file_handler.setFormatter(file_formater)

logger_payment.addHandler(file_handler)
logger_payment.addHandler(console_handler)

#logger customer
console_handler_customer=logging.StreamHandler()
console_handler_customer.setLevel(logging.WARNING)

file_handler_customer=logging.FileHandler('app_customer.log')
file_handler_customer.setLevel(logging.DEBUG)

console_formater_customer=logging.Formatter("%(levelname)s | %(message)s")
file_formater_customer=logging.Formatter("%(asctime)s | %(levelname)s | %(name)s |%(message)s")

console_handler_customer.setFormatter(console_formater_customer)
file_handler_customer.setFormatter(file_formater_customer)

logger_customer.addHandler(file_handler_customer)
logger_customer.addHandler(console_handler_customer)

logger_payment.debug("Debugging")
logger_payment.info("Information")
logger_payment.warning("Warning")
logger_payment.error("Error")
logger_payment.critical("Critical")
print("=====================")
logger_customer.debug("Debugging")
logger_customer.info("Information")
logger_customer.warning("Warning")
logger_customer.error("Error")
logger_customer.critical("Critical")