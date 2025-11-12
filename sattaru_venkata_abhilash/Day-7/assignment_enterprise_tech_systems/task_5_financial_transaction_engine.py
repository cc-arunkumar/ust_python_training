# Task 5 — Financial Transaction Engine
# Domain: Banking & Fintech
# Business Requirement:
# UST Finance Solutions team needs a transaction system.

# 1. Transaction (base class)
class Transaction:
    def __init__(self, txn_id, amount, status):
        self.txn_id = txn_id
        self.amount = amount
        self.status = status

    def process(self):
        print(f"Transaction ID: {self.txn_id}")
        print(f"Transaction Amount: ₹{self.amount}")
        print(f"Transaction Status: {self.status}")

# 2. CardTransaction inherits from Transaction
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status, card_number):
        Transaction.__init__(self, txn_id, amount, status)
        self.card_number = card_number

    def verify_card(self):
        if len(str(self.card_number)) == 16:
            print(f"Card Number {self.card_number} verified successfully")
        else:
            print(f"Card Number {self.card_number} not verified")

# 3. OnlinePayment inherits from Transaction
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status, payment_gateway):
        Transaction.__init__(self, txn_id, amount, status)
        self.payment_gateway = payment_gateway

    def verify_gateway(self):
        if self.status == "active":
            print("Gateway Verified")
        else:
            print("Gateway Verification Failed")

# 4. InternationalCardPayment inherits from both CardTransaction and OnlinePayment
class InternationalCardPayment(CardTransaction, OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number, payment_gateway):
        CardTransaction.__init__(self, txn_id, amount, status, card_number)
        OnlinePayment.__init__(self, txn_id, amount, status, payment_gateway)

# Object Creation
transaction = CardTransaction(78901, 12000, "active", 4567123498761234)
transaction1 = OnlinePayment(987654, 850, "active", "Google Pay")

# Method Calls
transaction.verify_card()
transaction1.verify_gateway()


# Sample Output:
# Card Number 4567123498761234 verified successfully
# Gateway Verified