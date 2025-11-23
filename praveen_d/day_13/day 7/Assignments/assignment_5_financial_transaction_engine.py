# Financial Transaction Engine

class Transaction:
    def __init__(self, txn_id, amount):
        self.txn_id = txn_id
        self.amount = amount
        self.status = "PENDING"


class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, card_number):
        super().__init__(txn_id, amount)
        self.card_number = card_number

    def verify_card(self):
        return len(self.card_number) == 16  

    def process(self):
        if self.verify_card():
            self.status = "SUCCESS"
        else:
            self.status = "FAILED "


class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, gateway):
        super().__init__(txn_id, amount)
        self.gateway = gateway

    def verify_gateway(self):
        return self.gateway.lower() in ["paypal", "stripe", "razorpay","Gpay"]

    def process(self):
        if self.verify_gateway():
            self.status = "SUCCESS"
        else:
            self.status = "FAILED "


# Multiple inheritance to reuse both verifications
class InternationalCardPayment(CardTransaction, OnlinePayment):
    def __init__(self, txn_id, amount, card_number, gateway):
        Transaction.__init__(self, txn_id, amount)
        self.card_number = card_number
        self.gateway = gateway

    def process(self):
        if self.verify_card() and self.verify_gateway():
            self.status = "SUCCESS"
        else:
            self.status = "FAILED "


card_transaction = CardTransaction(101, 5000, "8272536250123456")
card_transaction.process()
print(card_transaction.txn_id, card_transaction.status)

online_payments = OnlinePayment(102, 2000, "razorpay")
online_payments.process()
print(online_payments.txn_id, online_payments.status)

inter_card_pay = InternationalCardPayment(103, 8000, "9333567890949456", "Stripe")
inter_card_pay.process()
print(inter_card_pay.txn_id, inter_card_pay.status)

# Sample output:
# 101 SUCCESS
# 102 SUCCESS
# 103 SUCCESS
