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


class Transction:
    def __init__(self,txn_id,amount,status):
        self.txn_id = txn_id
        self.amount = amount
        self.status = status
        
    def process(self):
        print(f"Transaction Status: {self.status}")
        
class CardTransaction(Transction):
    def __init__(self, txn_id, amount, status,card_number):
        Transction.__init__(self,txn_id, amount, status)
        self.card_number = card_number
        
    def verify_card(self):
        print(f"Card number {self.card_number} has Verified")
        
class OnlinePayment(Transction):
    def __init__(self, txn_id, amount, status,payment_gateway):
        Transction.__init__(self,txn_id, amount, status)
        self.payment_gateway = payment_gateway
        
    def verify_gateway(self):
        print(f"{self.payment_gateway} gateway has verified")
        
class InternationalCardPayment(CardTransaction,OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number,payment_gateway):
        CardTransaction.__init__(self,txn_id, amount, status, card_number)
        OnlinePayment.__init__(self,txn_id, amount, status, payment_gateway)
        
# Creating objects for all classes
transaction = Transction(103,10000,"Active")   
card = CardTransaction(104,30000,"Active",82717649809843)
card.verify_card()
online = OnlinePayment(105,40000,"Active","International")     
online.verify_gateway()

international = InternationalCardPayment(102,20000,"Active",13653725176,"International")
international.verify_card()
international.verify_gateway()

# output

# Card number 82717649809843 has Verified
# International gateway has verified
# Card number 13653725176 has Verified
# International gateway has verified