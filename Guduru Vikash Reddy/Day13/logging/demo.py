import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("logging started")
 
logging.basicConfig(
    level=logging.DEBUG,
    format=" %(message)s|%(asctime)s | %(levelname)s | %(name)s | line->%(lineno)d "
)
 
logging.debug("logging debug working")
logging.info("logging info working")
paymentloger=logging.getLogger("payment services")
customerloger=logging.getLogger("customer services")
paymentloger.info("payment services")
customerloger.info("customer services")

#  logging debug working|2025-11-19 11:10:26,447 | DEBUG | root | line->10 
#  logging info working|2025-11-19 11:10:26,447 | INFO | root | line->11 
#  payment services|2025-11-19 11:10:26,447 | INFO | payment.services | line->14 
#  customer services|2025-11-19 11:10:26,447 | INFO | customer.services | line->15 