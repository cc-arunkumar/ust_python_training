# Task 5 — Financial Transaction Engine
# Domain: Banking & Fintech

# Base class
class Transaction:
    def __init__(self, txn_id, amount, status):
        self.txn_id = txn_id
        self.amount = amount
        self.status = status

    def get_details(self):
        print(f"Transaction id is: {self.txn_id}")
        print(f"Amount is: {self.amount}")
        print(f"Status of transaction is: {self.status}")

# Subclass 1 — CardTransaction
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status, card_number):
        super().__init__(txn_id, amount, status)
        self.card_number = card_number

    def verify_card(self):
        print(f"Card number: {self.card_number}")


# Subclass 2 - OnlinePayment
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status, payment_gateway):
        super().__init__(txn_id, amount, status)
        self.payment_gateway = payment_gateway

    def verify_gateway(self):
        print(f"Payment gateway: {self.payment_gateway}")

# InternationalCardPayment class
class InternationalCardPayment(CardTransaction, OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number, payment_gateway):
        # initialize the common base once
        Transaction.__init__(self, txn_id, amount, status)
        # then set both extras
        self.card_number = card_number
        self.payment_gateway = payment_gateway

    def show_all(self):
        self.get_details()
        self.verify_card()
        self.verify_gateway()

#testing
all_txn = InternationalCardPayment(101, 30000, "Active", 1002938, "Approved")
print("-----International Card Gateway-----")
all_txn.show_all()

# sample output:
# -----International Card Gateway-----
# Transaction id is: 101
# Amount is: 30000
# Status of transaction is: Active
# Card number: 1002938
# Payment gateway: Approved
