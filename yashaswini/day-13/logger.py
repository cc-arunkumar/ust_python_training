#logger file for payment
import logging

logger = logging.getLogger("app.payment")
logger.setLevel(logging.INFO)

#console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

#File
file_handler = logging.FileHandler("app.payment.log")
file_handler.setLevel(logging.INFO)

console_format = logging.Formatter("%(levlname)s | %(message)s | %(lineno)d")
file_format = logging.Formatter("%(asctime)s | %(levelname)s | %(messade)s")

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This is a DEBUG message for payment")
logger.info("This is an INFO message for payment")
logger.warning("This is a WARNING message for payment")
logger.error("This is ERROR mesaage for payment")




#logger file for customer
import logging

logger = logging.getLogger("app.customer")
logger.setLevel(logging.INFO)

#console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

#File
file_handler = logging.FileHandler("app.customer.log")
file_handler.setLevel(logging.DEBUG)

console_format = logging.Formatter("%(levlname)s | %(message)s | %(lineno)d")
file_format = logging.Formatter("%(asctime)s | %(levelname)s | %(messade)s")

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This is a DEBUG message for customer")
logger.info("This is an INFO message for customer")
logger.warning("This is a WARNING message for customer")
logger.error("This is ERROR mesaage for customer")