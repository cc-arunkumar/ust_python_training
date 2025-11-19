import logging

# logging.basicConfig(level=logging.INFO)
logging.info("Logger Started")
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s | %(levelname)s | %(name)s | line: %(lineno)d | %(message)s"
                    )
logging.debug("Debugging is working")