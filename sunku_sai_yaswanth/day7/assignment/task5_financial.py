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
# ⚙️ Task: Create a design where the international payment type can access both
# card verification and gateway verification logic — without duplication.
# �� Hint: You might need a hybrid design (combination of multiple and multilevel
# inheritance).



class Transaction():
    def __init__(self,txn_id , amount , status):
        self.txn_id=txn_id
        self.amount=amount
        self.status=status
    def process(self):
        print(f"Transaction id: {self.txn_id}")
        print(f"Transaction amount: {self.amount}")
        print(f"Transaction status: {self.status}")
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status,card_number):
        Transaction.__init__(self,txn_id, amount, status)
        self.card_number=card_number
    def verify_card(self):
        if len(str(self.card_number))==16:
            print(f"the card is verified")
        else:
            print("card not verified")
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status,gateway):
        Transaction.__init__(self,txn_id, amount, status)
        self.gateway=gateway
    def verify_gateway(self):
        if self.gateway=="verified":
            print("gateway is cheaked and the card is verified ")
        else:
            print("gateway is cheaked and not vified")
class  InternationalCardPayment(CardTransaction,OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number,gateway):
        CardTransaction.__init__(self,txn_id, amount, status, card_number)
        OnlinePayment.__init__(self, txn_id, amount, status,gateway)

card=CardTransaction(10111,1000000,'yes',1234567899876543)
online=OnlinePayment(101112,230000,'yes','verified')

card.verify_card()
online.verify_gateway()
            
# output
# the card is verified
# gateway is cheaked and the card is verified 
        