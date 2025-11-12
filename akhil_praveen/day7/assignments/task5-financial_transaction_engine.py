# UST Finance Solutions team needs a transaction system.
# 1. Transaction (base class):
# txn_id ,  amount, status
# Method: process()
# 2. CardTransaction inherits from Transaction
# Has card number, method: verify_card()
# 3. OnlinePayment inherits from Transaction
# Has payment gateway, method: verify_gateway()
# 4. The system introduces InternationalCardPayment, which is:
# A combination of both card and online payment
# Needs to reuse both verification methods

# Parent class
class Transaction:
    def __init__(self,txn_id,amount,status):
        self.txn_id=txn_id
        self.amount=amount
        self.status=status
    def process(self):
        print(f"id: {self.txn_id}")
        print(f"Amount: {self.amount}")
        print(f"status: {self.status}")
        
# child class
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status,card_number):
        Transaction.__init__(self,txn_id, amount, status)
        self.card_number=card_number
    def verify_card(self):
        self.process()
        print(f"Card number:{self.card_number}")
        
# child class
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status,payment_gateway):
        Transaction.__init__(self,txn_id, amount, status)
        self.payment_gateway=payment_gateway
        
    def verify_gateway(self):
        self.process()
        print(f"Payment Gateway:{self.payment_gateway}")

# child class by multiple inheritance
class InternationalCardPayment(CardTransaction,OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number,payment_gateway):
        CardTransaction.__init__(self,txn_id, amount, status, card_number)
        OnlinePayment.__init__(self, txn_id, amount, status,payment_gateway)
    
    def display(self):
        self.process()
        print(f"Card number:{self.card_number}")
        print(f"Payment Gateway:{self.payment_gateway}")
    
# Object creation and getting info
inter1 = InternationalCardPayment(101,1000,"success","asf123249","UPI")
inter1.display()

# Output
# id: 101
# Amount: 1000
# status: success
# Card number:asf123249
# Payment Gateway:UPI