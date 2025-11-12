# Task 5 — Financial Transaction Engine
# Domain: Banking & Fintech
# Business Requirement:
# UST Finance Solutions team needs a transaction system.
# 1. Transaction (base class):
# txn_id , amount , status
# Method: process()

class Transaction:
    def __init__(self,txn_id,amount,status):
        self.txn_id=txn_id
        self.amount=amount
        self.status=status
    
    def process(self):
        print("Transaction ID: ",self.txn_id)
        print("Amount: ",self.amount)
        print("Status :",self.status)

# 2. CardTransaction inherits from Transaction
# Has card number, method: verify_card()
class CardTranaction(Transaction):
    def __init__(self,txn_id,amount,status,card_number):
        Transaction.__init__(self,txn_id,amount,status)
        self.card_number=card_number
    
    def verify_card(self):
        if self.status=="Active":
            print("Verified")
        else:
            print("Un Verified")

# 3. OnlinePayment inherits from Transaction
# Has payment gateway, method: verify_gateway()
class OnlinePayment(Transaction):
    def __init__(self,txn_id,amount,status,payment_gateway):
        Transaction.__init__(self,txn_id,amount,status)
        self.payment_gateway=payment_gateway
    
    def verify_gateway(self):
        if self.status=="Active":
            print("Verified")
        else:
            print("Un Verified")
# 4. The system introduces InternationalCardPayment, which is:
# A combination of both card and online payment
# Needs to reuse both verification methods
class InternationalCardPayment(CardTranaction,OnlinePayment):
    def __init__(self,txn_id,amount,status,card_number,payment_gateway):
        CardTranaction.__init__(self,txn_id,amount,status,card_number)
        OnlinePayment.__init__(self,txn_id,amount,status,payment_gateway)
        
        
pay1=CardTranaction(11,45000,"Active",890678)
pay1.verify_card()

pay2=OnlinePayment(13,4000,"InActive",890678)
pay2.verify_gateway()


pay1=InternationalCardPayment(12,5000,"Active",890008,"Phonepay")
pay1.verify_card()
pay1.verify_gateway()

#Sample output
# Verified
# Un Verified
# Verified   
# Verified 