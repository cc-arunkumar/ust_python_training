# task 5 — Financial Transaction Engine
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
# inheritance)

class Transaction:
    def __init__(self,txn_id , amount , status):
        self.txn_id=txn_id
        self.amount=amount
        self.status=status
    def process(self):
        print(f"the status of the transaction is {self.status}")
        
# CardTransaction extends Transaction
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status,card_number):
        Transaction.__init__(self,txn_id, amount, status)
        self.card_number=card_number
    def verify_card(self):
        print(f"The {self.card_number} is verified")

#ONlinePayment extends Transaction
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status,payment_gateway):
        Transaction.__init__(self,txn_id, amount, status)
        self.payment_gateway=payment_gateway
    def verify_gateway(self):
        print(f"The give gateway {self.payment_gateway} is verified")
# InternationalCardPayment extends CardTransaction,OnlinePayment
class InternationalCardPayment(CardTransaction,OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number,payment_gateway):
        CardTransaction.__init__(self,txn_id, amount, status, card_number)
        OnlinePayment.__init__(self, txn_id, amount, status,payment_gateway)
        



#creating the objects and calling

InternationalCard=InternationalCardPayment(9087,90000,"Succesful",4567456789,"Phonepay")
InternationalCard.verify_card()
InternationalCard.verify_gateway()


# sample execution
# The 4567456789 is verified
# The give gateway Phonepay is verified