"""
Create a design where the international payment type can access both card verification and gateway verification logic — without duplication.
"""

class Transaction:
    def __init__(self,txn_id , amount , status):
        self.txn_id=txn_id
        self.amount=amount
        self.status=status
    
    def process(self):
        print(f"The Transaction id {self.txn_id} of Amount Rs.{self.amount} is {self.status}")

# Inherits From Transaction
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status,card_number):
        Transaction.__init__(self,txn_id, amount, status)
        self.card_number=card_number
    
    def verify_card(self):
        if type(self.card_number) == int:
            print("Card Verification Sucessful")

# Inherits from Transaction
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status,payment_gateway):
        Transaction.__init__(self,txn_id, amount, status)
        self.payment_gateway=payment_gateway

    def verify_gateway(self):
        if self.payment_gateway=="UPI":
            print(f"You are using {self.payment_gateway} that is Verified")


# Inherting from Both CardTransaction and OnlinePayment Class (--HYBRID---)
class InternationalCardPayment(CardTransaction,OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number,payment_gateway):
        CardTransaction.__init__(self, txn_id, amount, status,card_number)
        OnlinePayment.__init__(self, txn_id, amount, status,payment_gateway)
        self.payment_gateway=payment_gateway
    
    def process_international_payment(self):
        self.verify_card()
        self.verify_gateway()
        self.process()
        print("International Payment Gateway Verified")

        
# txn_id, amount, status, card_number,payment_gateway
icp=InternationalCardPayment(21,1000,"Sucessful",12345,"UPI")

icp.process_international_payment() # this function call the Entire functions that are created in those 3 Classes

"""
SAMPLE OUTPUT

Card Verification Sucessful
You are using UPI that is Verified
The Transaction id 21 of Amount Rs.1000 is Sucessful
International Payment Gateway Verified
"""