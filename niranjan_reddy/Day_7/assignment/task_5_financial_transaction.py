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


# 1. Transaction (base class):
# txn_id , amount , status
# Method: process()

class Transaction:
    def __init__(self,txn_id , amount , status):
        self.txn_id=txn_id 
        self.amount=amount
        self.status=status
    
    def process(self):
        print(f"Transaction  id:{self.txn_id}")
        print(f"Transaction  amount:{self.amount}")
        print(f"Transaction  status:{self.status}")

# 2. CardTransaction inherits from Transaction
# Has card number, method: verify_card()

class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status,card_number):
        Transaction.__init__(self,txn_id, amount, status)
        self.card_number=card_number
    def verify_card(self):
        if len(str(self.card_number))==16:
            print(f"Card Number {self.card_number} verified Successfully")
        else:
            print(f"Card Number {self.card_number} not verified")

# 3. OnlinePayment inherits from Transaction
# Has payment gateway, method: verify_gateway()

class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status,payment_gateway):
        Transaction.__init__(self,txn_id, amount, status)
        self.payment_gateway=payment_gateway

    def verify_gateway(self):
        if self.status=="active":
            print("Gate Verified")
        else:
            print("Gate verification failed")


# 4. The system introduces InternationalCardPayment, which is:
# A combination of both card and online payment
# Needs to reuse both verification methods

class InternationalCardPayment(CardTransaction,OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number,payment_gateway):
        CardTransaction.__init__(self,txn_id, amount, status, card_number)
        OnlinePayment.__init__(self, txn_id, amount, status,payment_gateway)

transaction=CardTransaction(12344,3500,"active",9234567898765456)
transaction1=OnlinePayment(2353216,200,"active","phone pay")
transaction.verify_card()
transaction1.verify_gateway()

# Sample output
# Card Number 9234567898765456 verified Successfully
# Gate Verified