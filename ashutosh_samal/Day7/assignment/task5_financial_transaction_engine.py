#Task 5 — Financial Transaction Engine
class Transaction:
    def __init__(self,txn_id , amount , status):
        self.txn_id = txn_id
        self.amount = amount
        self.status = status
        
    def process(self):
        print("Transaction ID: ",self.txn_id)
        print("Amount: ",self.amount)
        print("Status :",self.status)

#creation of card transaction class
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status):
        Transaction.__init__(self,txn_id, amount, status)
    
    #function to verify card
    def verify_card(self):
        if self.status == "Active":
            print("Verified Card")
        else:
            print("Failed Card Verification")

#creation of online payment class    
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status,payment_gateway):
        Transaction.__init__(self,txn_id, amount, status)
        self.payment_gateway = payment_gateway
    
    #function to verify gateway
    def verify_gateway(self):
        if self.status == "Active":
            print("Gateway Verified")
        else:
            print("Failed Gateway Verification")

#creation of InternationalCardPayment class
class InternationalCardPayment(CardTransaction,OnlinePayment):
    def __init__(self, txn_id, amount, status,payment_gateway):
        OnlinePayment.__init__(self,txn_id, amount, status,payment_gateway)
        CardTransaction.__init__(self, txn_id, amount, status)
        

pay1=CardTransaction("T10",45000,"Active")
pay1.verify_card()

pay2=OnlinePayment("T103",4000,"InActive","VISA")
pay2.verify_gateway()


pay3=InternationalCardPayment("T120",50000,"Active","MasterCard")
pay3.verify_card()
pay3.verify_gateway()

#Sample Execution
# Verified Card
# Failed Gateway Verification
# Verified Card
# Gateway Verified