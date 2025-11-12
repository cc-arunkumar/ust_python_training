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
#  Hint: You might need a hybrid design (combination of multiple and multilevel
# inheritance).


# Base class
class Transaction:
    def __init__(self, txn_id, amount, status):
        self.txn_id = txn_id
        self.amount = amount
        self.status = status

    def process(self):
        print(f"Processing transaction {self.txn_id} of ₹{self.amount} — Status: {self.status}")

# CardTransaction class
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status, card_number):
        Transaction.__init__(self, txn_id, amount, status)
        self.card_number = card_number

    def verify_card(self):
        print(f"Verifying card number: {self.card_number}")

# OnlinePayment class
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status, payment_gateway):
        Transaction.__init__(self, txn_id, amount, status)
        self.payment_gateway = payment_gateway

    def verify_gateway(self):
        print(f"Verifying payment gateway: {self.payment_gateway}")

# InternationalCardPayment class (inherits from both)
class InternationalCardPayment(CardTransaction, OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number, payment_gateway):
        CardTransaction.__init__(self, txn_id, amount, status, card_number)
        OnlinePayment.__init__(self, txn_id, amount, status, payment_gateway)

    def show_details(self):
        print(f"International Transaction ID: {self.txn_id}")
        print(f"Amount: ₹{self.amount}, Status: {self.status}")
        print(f"Card: {self.card_number}, Gateway: {self.payment_gateway}")

# Test Transaction
t = Transaction("E25", 5000, "Approved")
t.process()
print("\n---")

ct = CardTransaction("E31", 750677, "Approved", "1234-67777")
ct.process()
ct.verify_card()

print("\n---")

# Test olinePaymentOn
op = OnlinePayment("E45", 1200, "Failed", "PayFast")
op.process()
op.verify_gateway()

print("\n---")

# Test InternationalCardPayment
icp = InternationalCardPayment("E45", 10000, "Processing", "888888-666666", "phonepay")
icp.process()
icp.verify_card()
icp.verify_gateway()
icp.show_details()

#output
# Processing transaction E25 of ₹5000 — Status: Approved

# ---
# Processing transaction E31 of ₹750677 — Status: Approved
# Verifying card number: 1234-67777

# ---
# Processing transaction E45 of ₹1200 — Status: Failed
# Verifying payment gateway: PayFast

# ---
# Processing transaction E45 of ₹10000 — Status: Processing
# Verifying card number: 888888-666666
# Verifying payment gateway: phonepay
# International Transaction ID: E45
# Amount: ₹10000, Status: Processing
# Card: 888888-666666, Gateway: phonepay
