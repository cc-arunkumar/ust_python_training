import logging

logger= logging.getLogger("app")
logger.setLevel(logging.WARNING)
logger
ch=logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

logger.debug("This is debug ")
logger.info("thsi info ")
logger.warning("tis is warning")
logger.error("tis is error")
print("thsnkyou")
