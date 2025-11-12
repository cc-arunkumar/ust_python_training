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

# Define the Transaction class         

class Transaction:
    def __init__(self,txn_id , amount , status):
        self.txn_id = txn_id 
        self.amount = amount 
        self.status = status 
        
    def process(self):
        print("Processing your Transaction...")

# Define the CardTransaction class         
class CardTransaction(Transaction):
    def __init__(self,txn_id,amount,status,card_number):
        Transaction.__init__(self,txn_id,amount,status)
        self.card_number = card_number
    
    def verify_card(self):
        if self.status=="Active":
            print("Card Verified Succesfully!")
        else:
            print("Card Not Verified!")

# Define the OnlinePayment class         
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status,payment_gateway):
        Transaction.__init__(self,txn_id, amount, status)
        self.payment_gateway = payment_gateway 
    
    def verify_gateway(self):
        if self.status=="Active":
            print("Gateway Verified Succesfully!")
        else:
            print("Gateway Not Verified!")
    
# Define the InternationalCardPayment class         
class InternationalCardPayment(OnlinePayment,CardTransaction):
    def __init__(self, txn_id, amount, status,payment_gateway,card_number):
        OnlinePayment.__init__(self, txn_id, amount, status,payment_gateway)
        CardTransaction.__init__(self,txn_id,amount,status,card_number)
        
payment1 = InternationalCardPayment('TXN1234567890123456',5000,'Active','SBI','3425322431')
payment1.process()
payment1.verify_card()
payment1.verify_gateway()
   
    
#Sample Output
# Processing your Transaction...
# Card Verified Succesfully!
# Gateway Verified Succesfully!