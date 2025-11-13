#  Task 5 — Financial Transaction Engine
#  Domain: Banking & Fintech
#  Business Requirement:
#  UST Finance Solutions team needs a transaction system.
#   
# Transaction (base class):
#  txn_id , 
# amount , 
# status
#  Method: 
# process()
#   
# CardTransaction inherits from 
# Transaction
#  Has card number, method: 
# verify_card()
#   
# OnlinePayment inherits from 
# Transaction
#  Has payment gateway, method: 
# verify_gateway()
#   The system introduces InternationalCardPayment, which is:
#  A combination of both card and online payment
#  Needs to reuse both verification method

# Base class
class Transaction:
    def __init__(self, txn_id, amount, status):
        self.txn_id = txn_id
        self.amount = amount
        self.status = status

    def process(self):
        print(f"Processing transaction {self.txn_id} for amount ₹{self.amount} — Status: {self.status}")


# CardTransaction inherits from Transaction
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, status, card_number):
        Transaction.__init__(self, txn_id, amount, status)
        self.card_number = card_number

    def verify_card(self):
        print(f"Verifying card number {self.card_number} for transaction {self.txn_id}")


# OnlinePayment inherits from Transaction
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, status, gateway):
        Transaction.__init__(self, txn_id, amount, status)
        self.gateway = gateway

    def verify_gateway(self):
        print(f"Verifying payment gateway '{self.gateway}' for transaction {self.txn_id}")


# InternationalCardPayment combines both CardTransaction and OnlinePayment
class InternationalCardPayment(CardTransaction, OnlinePayment):
    def __init__(self, txn_id, amount, status, card_number, gateway):
        CardTransaction.__init__(self, txn_id, amount, status, card_number)
        OnlinePayment.__init__(self, txn_id, amount, status, gateway)

    def process(self):
        print(f"Processing international card payment {self.txn_id} for ₹{self.amount}")
        self.verify_card()
        self.verify_gateway()
        print(f"Transaction status: {self.status}")



if __name__ == "__main__":
    txn1 = CardTransaction("TXN1001", 5000, "Pending", "1234-5678-9012-3456")
    txn1.process()
    txn1.verify_card()

    txn2 = OnlinePayment("TXN1002", 7500, "Success", "PayFast")
    txn2.process()
    txn2.verify_gateway()

    txn3 = InternationalCardPayment("TXN1003", 12000, "Pending", "9876-5432-1098-7654", "GlobalPay")
    txn3.process()
    
# Output
# Processing transaction TXN1001 for amount ₹5000 — Status: Pending
# Verifying card number 1234-5678-9012-3456 for transaction TXN1001
# Processing transaction TXN1002 for amount ₹7500 — Status: Success
# Verifying payment gateway 'PayFast' for transaction TXN1002
# Processing international card payment TXN1003 for ₹12000
# Verifying card number 9876-5432-1098-7654 for transaction TXN1003
# Verifying payment gateway 'GlobalPay' for transaction TXN1003
# Transaction status: Pending