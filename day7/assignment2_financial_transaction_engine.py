# Task 5 — Financial Transaction Engine

# 1. Base class → Transaction
class Transaction:
    def __init__(self, txn_id, amount, status="Pending"):
        self.txn_id = txn_id
        self.amount = amount
        self.status = status

    def process(self):
        print(f"Transaction {self.txn_id}: Amount {self.amount}, Status {self.status}")


# 2. CardTransaction inherits from Transaction
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, card_number, status="Pending"):
        Transaction.__init__(self, txn_id, amount, status)
        self.card_number = card_number

    def verify_card(self):
        # Simple check: card number length must be 16
        if len(str(self.card_number)) == 16:
            print(f"Card {self.card_number} verified successfully.")
            return True
        else:
            print(f"Card {self.card_number} verification failed.")
            return False


# 3. OnlinePayment inherits from Transaction
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, gateway, status="Pending"):
        Transaction.__init__(self, txn_id, amount, status)
        self.gateway = gateway

    def verify_gateway(self):
        # Simple check: gateway must be one of supported
        supported_gateways = ["PayPal", "Stripe", "Razorpay"]
        if self.gateway in supported_gateways:
            print(f"Gateway {self.gateway} verified successfully.")
            return True
        else:
            print(f"Gateway {self.gateway} verification failed.")
            return False


# 4. InternationalCardPayment inherits both CardTransaction and OnlinePayment
class InternationalCardPayment(CardTransaction, OnlinePayment):
    def __init__(self, txn_id, amount, card_number, gateway, status="Pending"):
        # Initialize both parents
        CardTransaction.__init__(self, txn_id, amount, card_number, status)
        OnlinePayment.__init__(self, txn_id, amount, gateway, status)

    def process(self):
        print(f"International Transaction {self.txn_id}: Amount {self.amount}, Status {self.status}")
        card_ok = self.verify_card()
        gateway_ok = self.verify_gateway()
        if card_ok and gateway_ok:
            self.status = "Completed"
            print("International card payment processed successfully.")
        else:
            self.status = "Failed"
            print("International card payment failed.")


# Card Transaction
card_txn = CardTransaction("TXN1001", 5000, "1234567812345678")
card_txn.process()
card_txn.verify_card()

print("_________________________________________")

# Online Payment
online_txn = OnlinePayment("TXN1002", 3000, "PayPal")
online_txn.process()
online_txn.verify_gateway()

print("_________________________________________")

# International Card Payment
intl_txn = InternationalCardPayment("TXN1003", 10000, "9876543212345678", "Stripe")
intl_txn.process()


# Output

# Transaction TXN1001: Amount 5000, Status Pending
# Card 1234567812345678 verified successfully.
# _________________________________________
# Transaction TXN1002: Amount 3000, Status Pending
# Gateway PayPal verified successfully.
# _________________________________________
# International Transaction TXN1003: Amount 10000, Status Pending
# Card 9876543212345678 verified successfully.
# Gateway Stripe verified successfully.
# International card payment processed successfully.
