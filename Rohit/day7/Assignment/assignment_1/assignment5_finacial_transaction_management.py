# Financial Transaction Engine
# Domain: Banking & Fintech
# Business Requirement:
# UST Finance Solutions team needs a transaction system
# Base class representing a generic financial transaction
class Transaction:
    def __init__(self, txn_id, amount, status="Pending"):
        # Initialize transaction ID, amount, and default status ("Pending")
        self.txn_id = txn_id
        self.amount = amount
        self.status = status

    def process(self):
        # Print transaction details
        print(f"Processing Transaction ID: {self.txn_id}, Amount: {self.amount}, Status: {self.status}")


# Subclass representing transactions done via card
class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, card_number, status="Pending"):
        # Call parent (Transaction) constructor to initialize common attributes
        super().__init__(txn_id, amount, status)
        # Store card number specific to card transactions
        self.card_number = card_number

    def verify_card(self):
        # Simple validation: check if card number length is 16 digits
        if len(str(self.card_number)) == 16:
            print("Card verification successful.")
            return True
        else:
            print("Card verification failed.")
            return False


# Subclass representing online payments through gateways
class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, payment_gateway, status="Pending"):
        # Call parent (Transaction) constructor
        super().__init__(txn_id, amount, status)
        # Store payment gateway name
        self.payment_gateway = payment_gateway

    def verify_gateway(self):
        # Check if gateway is one of the recognized ones
        if self.payment_gateway.lower() in ["paypal", "stripe", "razorpay"]:
            print("Payment gateway verified.")
            return True
        else:
            print("Payment gateway not recognized.")
            return False


# Subclass representing international card payments
# Demonstrates multiple inheritance: inherits from both CardTransaction and OnlinePayment
class InternationalCardPayment(CardTransaction, OnlinePayment):
    def __init__(self, txn_id, amount, card_number, payment_gateway, status="Pending"):
        # Initialize both parent classes explicitly
        CardTransaction.__init__(self, txn_id, amount, card_number, status)
        OnlinePayment.__init__(self, txn_id, amount, payment_gateway, status)

    def process(self):
        # Print international transaction details
        print(f"International Transaction ID: {self.txn_id}, Amount: {self.amount}, Status: {self.status}")
        # Verify both card and payment gateway
        card_ok = self.verify_card()
        gateway_ok = self.verify_gateway()
        # Update status based on verification results
        if card_ok and gateway_ok:
            self.status = "Completed"
            print("International Card Payment processed successfully.")
        else:
            self.status = "Failed"
            print("International Card Payment failed.")


# Create a CardTransaction object with transaction details
card_txn = CardTransaction(
    txn_id="TXN1001",   # Transaction ID
    amount=5000,        # Transaction amount
    card_number=1234567812345678  # 16-digit card number
)

# Call process method from Transaction class to show transaction details
card_txn.process()

# Call verify_card method from CardTransaction class to validate card number
card_txn.verify_card()


# ====================sample output===============
# Processing Transaction ID: TXN1001, Amount: 5000, Status: Pending
# Card verification successful.
