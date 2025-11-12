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

#Main class
class Transaction:

    def __init__(self,txn_id,amount,status):
        self.txn_id = txn_id
        self.amount = amount
        self.status = status

    def process(self):
        print(f"Transaction ID : {self.txn_id}")
        print(f"Amount : {self.amount}")
        print(f"Status : {self.status}")

#Sub-class
class CardTransaction(Transaction):

    def __init__(self, txn_id, amount, status, card_no):
        Transaction.__init__(self,txn_id, amount, status)
        self.card_no = card_no

    def verify_card(self):
        self.process()
        print(f"Card No : {self.card_no}")

#Sub-class
class OnlinePayment(Transaction):

    def __init__(self, txn_id, amount, status, payment_gateway):
        Transaction.__init__(self,txn_id, amount, status)
        self.payment_gateway = payment_gateway
    
    def verify_gateway(self):
        self.process()
        print(f"Gateway : {self.payment_gateway}")

#Sub-class
class InternationalCardPayment(CardTransaction,OnlinePayment):

    def __init__(self, txn_id, amount, status, card_no, payment_gateway):
        CardTransaction.__init__(self,txn_id, amount, status, card_no)
        OnlinePayment.__init__(self,txn_id, amount, status, payment_gateway)
    
    def display(self):
        self.process()
        print(f"Card No : {self.card_no}")
        print(f"Gateway : {self.payment_gateway}")

#Creating the object
international = InternationalCardPayment("TVM-123",500000,"Payment Complete",876987421,"UPI")
international.display()

# --------------------------------------------------------------------------------------------

# Sample Output

# Transaction ID : TVM-123
# Amount : 500000
# Status : Payment Complete
# Card No : 876987421
# Gateway : UPI
