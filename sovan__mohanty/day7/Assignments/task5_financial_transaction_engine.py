#Task 5— Financial Transaction Engine
class Transaction:
    def __init__(self,txn_id,amount , status):
        self.txn_id=txn_id
        self.amount=amount
        self.status=status
    def process(self):
        print(f"Tax-id: ",self.txn_id)
        print(f"Amount: ",self.amount)
        print(f"Status: ",self.status)
#Creating Class Card Transaction
class CardTransaction(Transaction):
    def __init__(self,txn_id,amount , status,card):
        Transaction.__init__(self,txn_id,amount , status)
        self.card=card
        
    def verify_card(self):
        return len(str(self.card)) == 16
#Creating class Online Payment
class OnlinePayment(Transaction):
    def __init__(self,txn_id,amount , status,gateway):
        Transaction.__init__(self,txn_id,amount , status)
        self.gateway=gateway
    def verify_gateway(self):
        return self.gateway in ["Google Pay","Phone Pe"]
#Creating class International Card Payment
class InternationalCardPayment(CardTransaction,OnlinePayment):
    def __init__(self,txn_id,amount , status,card,gateway):
        CardTransaction.__init__(self,txn_id,amount,status,card)
        OnlinePayment.__init__(self,txn_id,amount , status,gateway)
    def full_verification(self):
        card_ok = self.verify_card()
        gateway_ok = self.verify_gateway()
        return card_ok and gateway_ok

# International card payment (hybrid)
intl_txn = InternationalCardPayment(203, 10000, "Active","9876543212345678", "Google Pay")
intl_txn.process()
print("Full verification:", intl_txn.full_verification())

#Sample Execution
# Tax-id:  203
# Amount:  10000
# Status:  Active
# Full verification: True