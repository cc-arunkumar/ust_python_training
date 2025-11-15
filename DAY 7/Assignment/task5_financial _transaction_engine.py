"""
Create a design where the international payment type can access both 
card verification and gateway verification logic — without duplication.
"""

# Base Transaction Class
class Transaction:
    def __init__(self, txn_id, amount, status):
        self.txn_id = txn_id              # Unique transaction ID
        self.amount = amount              # Transaction amount
        self.status = status              # Payment status
    
    # Show transaction summary
    def process(self):
        print(f"The Transaction id {self.txn_id} of Amount Rs.{self.amount} is {self.status}")



# Inherits from Transaction — handles card payments
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status, card_number):
        Transaction.__init__(self, txn_id, amount, status)   # Initialize base attributes
        self.card_number = card_number                        # Store card number
    
    # Verify card details
    def verify_card(self):
        if type(self.card_number) == int:
            print("Card Verification Sucessful")



# Inherits from Transaction — handles online gateway-based payments
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status, payment_gateway):
        Transaction.__init__(self, txn_id, amount, status)   # Initialize base transaction data
        self.payment_gateway = payment_gateway               # Store gateway
    
    # Verify payment gateway
    def verify_gateway(self):
        if self.payment_gateway == "UPI":
            print(f"You are using {self.payment_gateway} that is Verified")



# Hybrid Inheritance — Can access both card & online payment logic
class InternationalCardPayment(CardTransaction, OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number, payment_gateway):
        CardTransaction.__init__(self, txn_id, amount, status, card_number)   # Initialize card data
        OnlinePayment.__init__(self, txn_id, amount, status, payment_gateway) # Initialize gateway data
        self.payment_gateway = payment_gateway
    
    # Full international payment processing
    def process_international_payment(self):
        self.verify_card()        # Card verification
        self.verify_gateway()     # Gateway verification
        self.process()            # Base transaction process
        print("International Payment Gateway Verified")

        

# txn_id, amount, status, card_number, payment_gateway
icp = InternationalCardPayment(21, 1000, "Sucessful", 12345, "UPI")

# This function calls all required checks from multiple parent classes
icp.process_international_payment()

"""
SAMPLE OUTPUT

Card Verification Sucessful
You are using UPI that is Verified
The Transaction id 21 of Amount Rs.1000 is Sucessful
International Payment Gateway Verified
"""