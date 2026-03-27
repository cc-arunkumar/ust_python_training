import logging

#create logger
logger = logging.getLogger("app_payment.log")
logger.setLevel(logging.WARNING)

#Handlers where to go
#console
console_Handler =logging.StreamHandler()
console_Handler.setLevel(logging.DEBUG)

#file handler
file_Handler = logging.FileHandler("app_payment.log")
file_Handler.setLevel(logging.WARNING)

#formatte to logs
console_format = logging.Formatter("%(levelname)s| %(message)s | line: %(lineno)d")
file_format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

console_Handler.setFormatter(console_format)
file_Handler.setFormatter(file_format)

logger.addHandler(console_Handler)
logger.addHandler(file_Handler)

logger.debug("this is debug message")
logger.info("this is info message")
logger.warning("this is warning")
logger.error("this is error message")

#output
# DEBUG| this is debug message | line: 26
# INFO| this is info message | line: 27
# WARNING| this is warning | line: 28
# ERROR| this is error message | line: 29

print("**************")
print("log for customer payment")
import logging

logger = logging.getLogger("app_customer.log")
logger.setLevel(logging.DEBUG)

console_Handler = logging.StreamHandler()
logger.setLevel(logging.DEBUG)

file_Handler = logging.FileHandler("app_customer.log")
logger.setLevel(logging.DEBUG)

console_format = logging.Formatter(" %(levelname)s |%(message)s")
file_format = logging.Formatter("%(asctime)s |  %(levelname)s |%(message)s")

console_Handler.setFormatter(console_format)
file_Handler.setFormatter(file_format)

logger.addHandler(console_Handler)
logger.addHandler(file_Handler)

logger.info("these is info")
logger.debug("this is debug og customer")
logger.warning("this is warning of customer")
logger.error("this is error of customer")

# WARNING| this is warning | line: 28
# ERROR| this is error message | line: 29
# **************
# log for customer payment
#  INFO |these is info
#  DEBUG |this is debug og customer
#  WARNING |this is warning of customer
#  ERROR |this is error of customer