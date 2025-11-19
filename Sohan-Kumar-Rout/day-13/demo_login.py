#Debug:Level-10 :- Use of trace variable value or program flow  Ex-connecting to DB 
#Info : Level 20 :- show progress or actions performed Ex- user logged in 
#Warning : Level 30:- Something unexpected happen, might become a problem but program executes Ex-logger warning "low disc space"
#Error : level 40 :- A serious issue occured a part of program failed program continue running , a soecific part failed Ex- logger.error failed to read file 
#Critical : level 50 :- Program crashed (about to crash) . Immediate action req since system is unusable Ex- Logger.crirtical(server down)



import logging

# logging.basicConfig(level=logging.INFO)
# logging.info("Logger Started ")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime) s |  %(levelname)s  | %(name)s | line: %(lineno)d | %(message)s"
)
logging.info("Info level")
logging.debug("debugging working")

payment_logger=logging.getLogger("payment.services")
customer_logger=logging.getLogger("customer.services")
payment_logger.info("payment services started")
customer_logger.info("customer services started")

#Output
# 2025-11-19 18:45:30,755 |  INFO  | root | line: 18 | Info level
# 2025-11-19 18:45:30,755 |  DEBUG  | root | line: 19 | debugging working
# 2025-11-19 18:45:30,755 |  INFO  | payment.services | line: 23 | payment services started        
# 2025-11-19 18:45:30,756 |  INFO  | customer.services | line: 24 | customer services started

