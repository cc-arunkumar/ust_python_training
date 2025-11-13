#Assignment 5: Financial Transaction Engine

# Base class
class Transaction:
    def __init__(self, txn_id, amount, status):
        self.txn_id = txn_id
        self.amount = amount
        self.status = status

    def process(self):
        print(f"Processing Transaction ID: {self.txn_id} | Amount: ₹{self.amount} | Status: {self.status}")


class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status, card_number):
        Transaction.__init__(self,txn_id, amount, status)
        self.card_number = card_number

    def verify_card(self):
        print(f"Verifying card number: {self.card_number}")


class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status, gateway):
        Transaction.__init__(self,txn_id, amount, status)
        self.gateway = gateway

    def verify_gateway(self):
        print(f"Verifying payment gateway: {self.gateway}")


class InternationalCardPayment(CardTransaction, OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number, gateway):
        CardTransaction.__init__(self, txn_id, amount, status, card_number)
        OnlinePayment.__init__(self, txn_id, amount, status, gateway)

    def show_details(self):
        self.process()
        self.verify_card()
        self.verify_gateway()


card_txn = CardTransaction("TXN1001", 5000, "Pending", "1234-5678-9012-3456")
card_txn.process()
card_txn.verify_card()
print("----------------------------------")

online_txn = OnlinePayment("TXN2002", 7500, "Success", "PayPal")
online_txn.process()
online_txn.verify_gateway()
print("----------------------------------")

intl_txn = InternationalCardPayment("TXN3003", 12000, "Initiated", "9876-5432-1098-7654", "Stripe")
intl_txn.show_details()


#Output:
'''
Processing Transaction ID: TXN1001 | Amount: ₹5000 | Status: Pending
Verifying card number: 1234-5678-9012-3456
----------------------------------
Processing Transaction ID: TXN2002 | Amount: ₹7500 | Status: Success
Verifying payment gateway: PayPal
----------------------------------
Processing Transaction ID: TXN3003 | Amount: ₹12000 | Status: Initiated
Verifying card number: 9876-5432-1098-7654
Verifying payment gateway: Stripe
'''