import logging 

logger = logging.getLogger('app.payment')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app_payment.log')
file_handler.setLevel(logging.INFO)

console_formater = logging.Formatter("%(name)s | %(asctime)s | %(levelname)s | line: %(lineno)d")
file_formater = logging.Formatter("%(levelname)s | %(message)s | %(levelno)d")

console_handler.setFormatter(console_formater)
file_handler.setFormatter(file_formater)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This is Debug Message")
logger.info("This is Info")
logger.warning("this is warning")
logger.error("this is error")
logger.critical("this is critical")
print("Done App Check!")



logger = logging.getLogger('app.customer')
logger.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app_customer.log')
file_handler.setLevel(logging.INFO)

console_formater = logging.Formatter("%(name)s | %(asctime)s | %(levelname)s | line: %(lineno)d")
file_formater = logging.Formatter("%(levelname)s | %(message)s | %(levelno)d")

console_handler.setFormatter(console_formater)
file_handler.setFormatter(file_formater)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This is Debug Message")
logger.info("This is Info")
logger.warning("this is warning")
logger.error("this is error")
logger.critical("this is critical")
print("Done App Check!")