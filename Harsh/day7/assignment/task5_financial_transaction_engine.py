class Transaction:
    def __init__(self, txn_id, amount, status):
        self.txn_id = txn_id
        self.amount = amount
        self.status = status
    
    def process(self):
        print(f"The status of the Payment is {self.status}")
    

class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status, card_number):
        Transaction.__init__(self, txn_id, amount, status)
        self.card_number = card_number
    
    def verify_card(self):
        super().process()
        print(f"Verifying Card Number: {self.card_number}")
    
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status, payment_gateway):
        self.payment_gateway = payment_gateway
        Transaction.__init__(self, txn_id, amount, status)

    def verify_gateway(self):
        super().process()
        print(f"Verifying the Payment Gateway : {self.payment_gateway}")

class InternationalCardPayment(CardTransaction, OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number, payment_gateway):
        CardTransaction.__init__(self,txn_id, amount, status, card_number)
        OnlinePayment.__init__(self, txn_id, amount, status, payment_gateway)


t1 = Transaction(101, 5000, 'Success')
t1.process()
print("---------------------------------------------------")
ct1 = CardTransaction(102, 15000, 'Success', '1234-5678-9876-5432')
ct1.verify_card()
print("---------------------------------------------------")
op1 = OnlinePayment(103, 25000, 'Success', 'PayPal')
op1.verify_gateway()
print("---------------------------------------------------")
icp1 = InternationalCardPayment(104, 50000, 'Success', '9876-5432-1234-6789', 'Stripe')
icp1.process()
icp1.verify_card()
icp1.verify_gateway()


# The status of the Payment is Success
# ---------------------------------------------------
# Verifying Card Number: 1234-5678-9876-5432
# ---------------------------------------------------
# Verifying the Payment Gateway : PayPal
# ---------------------------------------------------
