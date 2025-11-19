import logging
logging.basicConfig(level=logging.INFO)
logging.info("logging started")

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s  | %(asctime)s | %(levelname)s | %(name)s | line->%(lineno)d"
)
logging.info("login info")
logging.debug("logging debug working")

payment_logger=logging.getLogger("payment.services")
customer_logger=logging.getLogger("customer.services")
payment_logger.info("payment services started")
customer_logger.info("customer services started")


# ✅ LEVEL 10 — DEBUG

# Purpose:

# Trace variable values

# Trace program execution flow

# Internal developer-level details

# Connecting to database, loading configs, etc.

# Example:

# Connecting to DB…

# x value = 42

# Function process_data() entered

# ✅ LEVEL 20 — INFO

# Purpose:

# Show progress

# Show actions being performed

# Normal behavior of the application

# Example:

# User logged in

# File uploaded successfully

# Processing completed

# ⚠️ LEVEL 30 — WARNING

# Purpose:

# Something unexpected happened

# Might become a problem later

# Program still continues to run

# Example:

# Low disk space

# API response delayed

# Logger warning: Retrying connection

# ❗ LEVEL 40 — ERROR

# Purpose:

# A serious issue occurred

# A part of the program failed

# Program continues but a specific task is broken

# Example:

# Failed to read file

# Database write failed

# Payment service timeout

# 💀 LEVEL 50 — CRITICAL

# Purpose:

# Program crashed or about to crash

# Extremely serious failure

# Immediate attention required

# System becomes unusable

# Example:

# Server down

# Critical system failure

# Memory corruption detected



