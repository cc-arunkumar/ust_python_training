
import logging

logger1=logging.getLogger("app_payment")
logger1.setLevel(logging.WARNING)


console_handler1=logging.StreamHandler()
console_handler1.setLevel(logging.DEBUG)


file_handler1=logging.FileHandler("app_payment.log")
file_handler1.setLevel(logging.WARNING)

console_formatter_1=logging.Formatter("%(levelname)s, |%(message)s |line: %(lineno)d |%(name)s")
file_formatter_1=logging.Formatter("%(levelname)s, |%(message)s |line: %(lineno)d, |%(name)s")

console_handler1.setFormatter(console_formatter_1)
file_handler1.setFormatter(file_formatter_1)

logger1.addHandler(console_handler1)
logger1.addHandler(file_handler1)


logger1.debug("DEBUG message")
logger1.info("INFO message")
logger1.warning("WARNING message")
logger1.error("ERROR message")
