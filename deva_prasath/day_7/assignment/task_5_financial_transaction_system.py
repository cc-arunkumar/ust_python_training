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


# Transaction class to store general transaction details
class Transaction:
    def __init__(self, txn_id, amount, status):
        self.txn_id = txn_id  # Transaction ID
        self.amount = amount  # Transaction amount
        self.status = status  # Transaction status 
    
    def process(self):
        # Process the transaction
        print("Processing the Transaction")

# CardTransaction class inherits from Transaction, adds card-specific verification
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status):
        super().__init__(txn_id, amount, status)  # Inherit from Transaction
        
    def verify_card(self):
        # Verify the card based on transaction status
        if self.status == "Approved":
            print("The card is verified")
        elif self.status == "Processing":
            print("The card is processing")
        else:
            print("Processing failed")

# OnlinePayment class inherits from Transaction, adds gateway specific verification
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status):
        super().__init__(txn_id, amount, status)  # Inherit from Transaction
    
    def verify_gateway(self):
        # Verify the gateway based on transaction status
        if self.status == "Approved":
            print("The gateway is verified")
        elif self.status == "Processing":
            print("The gateway is processing")
        else:
            print("Gateway failed")

# InternationalCardPayment class inherits from both CardTransaction and OnlinePayment
class InternationalCardPayment(CardTransaction, OnlinePayment):
    def __init__(self, txn_id, amount, status):
        super().__init__(txn_id, amount, status)  # Initialize both CardTransaction and OnlinePayment

# Object creation and method calls
ic = InternationalCardPayment(101, 10000, "Approved")  
ic.process()  # Process transaction
ic.verify_card()  # Verify card
ic.verify_gateway()  # Verify payment gateway
print("----------------------------")

ic2 = InternationalCardPayment(102, 20000, "Processing")  
ic2.process()  # Process transaction
ic2.verify_card()  # Verify card
ic2.verify_gateway()  # Verify payment gateway
print("----------------------------")

ic3 = InternationalCardPayment(103, 30000, "Rejected")  
ic3.process()  # Process transaction
ic3.verify_card()  # Verify card
ic3.verify_gateway()  # Verify payment gateway




#Sample output
# Processing the Transaction
# The card is verified
# The gateway  is verified
# ----------------------------
# Processing the Transaction
# The card  is processing
# The gateway  is processing
# ----------------------------
# Processing the Transaction
# Processing failed
# Gateway failed
