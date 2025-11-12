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
# Step 1: Define a base Transaction class with common transaction attributes
class Transaction:
    def __init__(self,txn_id,amount,status):
        self.txn_id=txn_id
        self.amount=amount
        self.status=status
    def  process(self):
        print("the process is:",self.status)

# Step 2: Create a CardTransaction subclass with card verification functionality
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status,cardnumber):
        Transaction.__init__(self,txn_id, amount, status)
        self.cardnumber=cardnumber
    def verify_card(self):
        print(f"The card  is:",self.cardnumber,"verified")

# Step 3: Create an OnlinePayment subclass with gateway verification
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status,payment_gateway):
        Transaction.__init__(self,txn_id, amount, status)
        self.payment_gateway=payment_gateway
    def verify_gateway(self):
        print(f"The gateway is:",self.payment_gateway)

# Step 4: Create a subclass combining CardTransaction and OnlinePayment for international card payments
class InternationalCardPayment(CardTransaction,OnlinePayment):
    def __init__(self, txn_id, amount, status, cardnumber,payment_gateway):
        CardTransaction.__init__(self,amount, status, cardnumber)
        OnlinePayment.__init__(self, txn_id, amount, status,payment_gateway)

# Step 5: Instantiate and test different transaction types
cardtransaction=CardTransaction(1010,40000,"completed","134256751231")
onlinepayment=OnlinePayment(1202,50000,"Not completed","Paytm")
transaction=Transaction(1231,30000,"Not completed")

cardtransaction.verify_card()
onlinepayment.verify_gateway()
transaction.process()
# sample output
# The card  is: 134256751231 verified
# The gateway is: Paytm
# the process is: Not completed

    


        