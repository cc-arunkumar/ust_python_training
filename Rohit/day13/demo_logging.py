import logging   # Import logging module

# Example (commented out):
# logging.basicConfig(level=logging.INFO)
# logging.info("This is an info message")

# Configure logging globally
logging.basicConfig(
    level=logging.INFO,   # Minimum level to capture (INFO and above)
    format="%(message)s |%(asctime)s | %(levelname)s | %(name)s | %(lineno)d"
    # Format includes:
    # - message text
    # - timestamp
    # - log level (INFO, WARNING, etc.)
    # - logger name
    # - line number
)

# Test logs
logging.debug("This is a debug message")   # Will NOT show (level is INFO)
logging.info("This is an info message")    # Will show

# Create named loggers for different modules/services
p_logger = logging.getLogger("payment.services")
c_logger = logging.getLogger("customer.services")

# Log messages from these loggers
p_logger.info("Payment service started")
c_logger.info("Customer service started")

# Comments explain log levels:
# DEBUG (10)    → trace variable values, detailed program flow (e.g., connecting to DB)
# INFO (20)     → progress or actions performed (e.g., user logged in)
# WARNING (30)  → unexpected situations, potential problems (e.g., low disk space)
# ERROR (40)    → serious issue, part of program failed (e.g., failed to read file)
# CRITICAL (50) → program crash or system unusable (e.g., server down)
