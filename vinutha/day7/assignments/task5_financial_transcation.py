# Task 5 — Financial Transaction Engine
# Domain: Banking & Fintech
# Business Requirement:
# UST Finance Solutions team needs a transaction system.
# 1. Transaction (base class):
# txn_id , amount , status
# Method: process()
# 2. CardTransaction inherits from Transaction
# Has card number, method: verify_card()
# 3. OnlinePayment inherits from Transaction
# Has payment gateway, method: verify_gateway()
# 4. The system introduces InternationalCardPayment, which is:
# A combination of both card and online payment
# Needs to reuse both verification methods
# Task: Create a design where the international payment type can access both
# card verification and gateway verification logic — without duplication.

# Base class

# Base class Transaction
class Transaction:
    def __init__(self, txn_id, amount, status):
        # Initialize common transaction attributes
        self.txn_id = txn_id
        self.amount = amount
        self.status = status

    def process(self):
        # Display transaction processing info
        print(f"Processing Transaction {self.txn_id} for ₹{self.amount} - Status: {self.status}")


# CardTransaction inherits from Transaction
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status, card_number):
        # Call Transaction constructor to initialize base attributes
        Transaction.__init__(self, txn_id, amount, status)
        # Add card-specific attribute
        self.card_number = card_number

    def verify_card(self):
        # Simulate card verification
        print(f"Verifying card number: {self.card_number}")


# OnlinePayment inherits from Transaction
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status, gateway):
        # Call Transaction constructor to initialize base attributes
        Transaction.__init__(self, txn_id, amount, status)
        # Add online payment-specific attribute
        self.gateway = gateway

    def verify_gateway(self):
        # Simulate gateway verification
        print(f"Verifying payment gateway: {self.gateway}")


# InternationalCardPayment inherits from both CardTransaction and OnlinePayment
# This demonstrates multiple inheritance
class InternationalCardPayment(CardTransaction, OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number, gateway):
        # Initialize CardTransaction part
        CardTransaction.__init__(self, txn_id, amount, status, card_number)
        # Initialize OnlinePayment part
        OnlinePayment.__init__(self, txn_id, amount, status, gateway)

    def show_details(self):
        # Call methods from Transaction, CardTransaction, and OnlinePayment
        self.process()        # From Transaction
        self.verify_card()    # From CardTransaction
        self.verify_gateway() # From OnlinePayment


# Sample usage
intl_txn = InternationalCardPayment("TXN9001", 5000, "Pending", "1234-5678-9012-3456", "PaySecure")

# Show details of the international card payment
intl_txn.show_details()

# #output
# Processing Transaction TXN9001 for ₹5000 - Status: Pending
# Verifying card number: 1234-5678-9012-3456
# Verifying payment gateway: PaySecure