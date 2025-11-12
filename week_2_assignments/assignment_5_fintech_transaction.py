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

class Transaction:
    def __init__(self,txn_id,amount,status):
        self.txn_id=txn_id
        self.amount=amount
        self.status=status
    def processed(self):
        print("processed...")
class CardTransaction(Transaction):
    def __init__(self,txn_id,amount,status,card_number):
        Transaction.__init__(self,txn_id,amount,status)
        self.card_number=card_number
    def verify_card(self):
        print("Card verified....")
class OnlinePayment(Transaction):
    def __init__(self,txn_id,amount,status,payment_gateway):
        Transaction.__init__(self,txn_id,amount,status)
        self.payment_gateway=payment_gateway
    def verify_gateway(self):
        print("verifying gateway...")
class InternationalCardPayment(CardTransaction,OnlinePayment):
    def __init__(self,txn_id,amount,status,card_number,payment_gateway):
        CardTransaction.__init__(self,txn_id,amount,status,card_number)
        OnlinePayment.__init__(self,txn_id,amount,status,payment_gateway)

international01=InternationalCardPayment(12234,12000.00,"online",1231231343443,"BHIM")
international01.verify_gateway()
international01.verify_card()

# verifying gateway...
# Card verified....