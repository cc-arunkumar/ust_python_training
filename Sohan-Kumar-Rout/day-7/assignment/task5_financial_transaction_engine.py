#Task 5: Financial Transaction Engine

#Code
class Transaction:
    def __init__(self,txn_id,amount,status):
        self.txn_id=txn_id
        self.amount=amount
        self.status=status
    def process(self):
        print(f"Tax-id {self.txn_id}")
        print(f"Tax Amount : {self.amount}")
        print(f"Status of the task : {self.status}")

class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status,card_number):
        Transaction.__init__(self,txn_id, amount, status)
        self.card_number=card_number
    def verify_card(self):
        if len(self.card_number) == 10:
            print(f"Valid Card ")
        else:
            print(f"Invalid Card ")
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status,online_payment):
        Transaction.__init__(self,txn_id, amount, status)
        self.online_payment=online_payment
        
    def verify_gateway(self):
        if self.online_payment in ["googlepay","PhonePay","Paytm"]:
            print("Valid payment")
        else:
            print("Invalid")

            
class InternationalCardPayment(CardTransaction,OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number,online_payment):
        CardTransaction.__init__(self,txn_id, amount, status, card_number)
        OnlinePayment.__init__(self,txn_id,amount,status,online_payment)
    def full_verification(self):
        
        valid_card=self.verify_card()
        valid_gateway=self.verify_gateway()
        return valid_card and valid_gateway
        
IntPCardPayment1=InternationalCardPayment(1022,3400,"Active","2334567890","googlepay")
IntPCardPayment1.process()
IntPCardPayment1.full_verification()

#Output
# Tax-id 1022
# Tax Amount : 3400
# Status of the task : Active
# Valid Card 
# Valid payment



        