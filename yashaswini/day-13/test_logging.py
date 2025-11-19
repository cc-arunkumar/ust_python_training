import logging

#create logger
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

#Handlers(where to you)
#console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

#File
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)

#3. formatters(how log looks)
console_format = logging.Formatter("%(levlname)s | %(message)s | %(lineno)d")
file_format = logging.Formatter("%(asctime)s | %(levelname)s | %(messade)s")

#4.attach handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

#5.use the logger
logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger.error("This is ERROR mesaage")

print("Done!check app.log")