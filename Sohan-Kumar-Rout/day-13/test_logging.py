import logging

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

console_handler=logging.StreamHandler()
console_handler.setLevel(logging.INFO)


file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

console_format = logging.Formatter("%(levelname)s | %(message)s | line : %(lineno)d")
file_format=logging.Formatter("%(asctime)s | %(levelname)s | %(message)s ")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)



logger.debug("This is debug message : ")
logger.info("This is info message ")
logger.warning("This is WARNING message")
logger.error("This is error message ")

print("Done ! check app.log ")


#Output
# INFO | This is info message  | line : 25
# WARNING | This is WARNING message | line : 26
# ERROR | This is error message  | line : 27
# Done ! check app.log

logger=logging.getLogger("app.customer")
logger.setLevel(logging.DEBUG)

console_handler=logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler=logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

console_format = logging.Formatter("%(levelname)s | %(message)s | line : %(lineno)d")
file_format=logging.Formatter("%(asctime)s | %(levelname)s | %(message)s ")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This is debug message : ")
logger.info("This is info message ")
logger.warning("This is WARNING message")
logger.error("This is error message ")
print("Done ! check app.log ")

#Output
# INFO | This is info message  | line : 57
# WARNING | This is WARNING message | line : 58
# ERROR | This is error message  | line : 59   
# Done ! check app.log 






