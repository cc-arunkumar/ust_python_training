import logging

logger=logging.getLogger("app")
logger.setLevel(logging.DEBUG)

console_handler=logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

file_handler=logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

console_formater=logging.Formatter("%(levelname)s | %(message)s")
file_formater=logging.Formatter("%(asctime)s | %(levelname)s | %(name)s |%(message)s")

console_handler.setFormatter(console_formater)
file_handler.setFormatter(file_formater)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug("Debugging")
logger.info("Information")
logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")