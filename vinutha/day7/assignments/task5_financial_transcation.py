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

class Transaction:
    def __init__(self, txn_id, amount, status):
        self.txn_id = txn_id
        self.amount = amount
        self.status = status

    def process(self):
        print(f"Processing Transaction {self.txn_id} for ₹{self.amount} - Status: {self.status}")

# CardTransaction inherits from Transaction
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status, card_number):
        Transaction.__init__(self, txn_id, amount, status)
        self.card_number = card_number

    def verify_card(self):
        print(f"Verifying card number: {self.card_number}")

# OnlinePayment inherits from Transaction
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status, gateway):
        Transaction.__init__(self, txn_id, amount, status)
        self.gateway = gateway

    def verify_gateway(self):
        print(f"Verifying payment gateway: {self.gateway}")

# InternationalCardPayment inherits from both CardTransaction and OnlinePayment
class InternationalCardPayment(CardTransaction, OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number, gateway):
        CardTransaction.__init__(self, txn_id, amount, status, card_number)
        OnlinePayment.__init__(self, txn_id, amount, status, gateway)

    def show_details(self):
        self.process()
        self.verify_card()
        self.verify_gateway()
intl_txn = InternationalCardPayment("TXN9001", 5000, "Pending", "1234-5678-9012-3456", "PaySecure")
intl_txn.show_details()

# #output
# Processing Transaction TXN9001 for ₹5000 - Status: Pending
# Verifying card number: 1234-5678-9012-3456
# Verifying payment gateway: PaySecure