#financial transaction engine


# Requirement:
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
# Task: Create a design where the international payment type can access both
# card verification and gateway verification logic — without duplication.
# Hint: You might need a hybrid design (combination of multiple and multilevel
# inheritance).


# Base class
class Transaction:
    def __init__(self, txn_id, amount, status):
        self.txn_id = txn_id
        self.amount = amount
        self.status = status

    def process(self):
        print(f"Processing transaction {self.txn_id} of amount Rs.{self.amount} with status '{self.status}'.")


# Mixin for card verification
class CardVerification:
    def __init__(self, card_number):
        self.card_number = card_number

    def verify_card(self):
        print(f"Verifying card number {self.card_number}")


# Mixin for gateway verification
class GatewayVerification:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def verify_gateway(self):
        print(f"Verifying payment gateway '{self.payment_gateway}'")


# CardTransaction inherits from Transaction and CardVerification
class CardTransaction(Transaction, CardVerification):
    def __init__(self, txn_id, amount, status, card_number):
        Transaction.__init__(self, txn_id, amount, status)
        CardVerification.__init__(self, card_number)

    def show_details(self):
        self.process()
        self.verify_card()


# OnlinePayment inherits from Transaction and GatewayVerification
class OnlinePayment(Transaction, GatewayVerification):
    def __init__(self, txn_id, amount, status, payment_gateway):
        Transaction.__init__(self, txn_id, amount, status)
        GatewayVerification.__init__(self, payment_gateway)

    def show_details(self):
        self.process()
        self.verify_gateway()


# InternationalCardPayment inherits from both verification mixins and Transaction
class InternationalCardPayment(Transaction, CardVerification, GatewayVerification):
    def __init__(self, txn_id, amount, status, card_number, payment_gateway):
        Transaction.__init__(self, txn_id, amount, status)
        CardVerification.__init__(self, card_number)
        GatewayVerification.__init__(self, payment_gateway)

    def show_details(self):
        self.process()
        self.verify_card()
        self.verify_gateway()


# Example usage
intl_txn = InternationalCardPayment(
    txn_id="TXN789",
    amount=15000,
    status="Pending",
    card_number="1234-5678-9012-3456",
    payment_gateway="PayGlobal"
)

intl_txn.show_details()


#o/p:
# Processing transaction TXN789 of amount Rs.15000 with status 'Pending'.
# Verifying card number 1234-5678-9012-3456
# Verifying payment gateway 'PayGlobal'