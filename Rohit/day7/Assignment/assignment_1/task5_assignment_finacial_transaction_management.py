class Transaction:
    def __init__(self, txn_id, amount, status="Pending"):
        self.txn_id = txn_id
        self.amount = amount
        self.status = status

    def process(self):
        print(f"Processing Transaction ID: {self.txn_id}, Amount: {self.amount}, Status: {self.status}")


class CardTransaction(Transaction):
    def __init__(self, txn_id, amount, card_number, status="Pending"):
        super().__init__(txn_id, amount, status)
        self.card_number = card_number

    def verify_card(self):
        if len(str(self.card_number)) == 16:  # simple check
            print("Card verification successful.")
            return True
        else:
            print("Card verification failed.")
            return False


class OnlinePayment(Transaction):
    def __init__(self, txn_id, amount, payment_gateway, status="Pending"):
        super().__init__(txn_id, amount, status)
        self.payment_gateway = payment_gateway

    def verify_gateway(self):
        if self.payment_gateway.lower() in ["paypal", "stripe", "razorpay"]:
            print("Payment gateway verified.")
            return True
        else:
            print("Payment gateway not recognized.")
            return False


class InternationalCardPayment(CardTransaction, OnlinePayment):
    def __init__(self, txn_id, amount, card_number, payment_gateway, status="Pending"):
        # Initialize both parents explicitly
        CardTransaction.__init__(self, txn_id, amount, card_number, status)
        OnlinePayment.__init__(self, txn_id, amount, payment_gateway, status)

    def process(self):
        print(f"International Transaction ID: {self.txn_id}, Amount: {self.amount}, Status: {self.status}")
        card_ok = self.verify_card()
        gateway_ok = self.verify_gateway()
        if card_ok and gateway_ok:
            self.status = "Completed"
            print("International Card Payment processed successfully.")
        else:
            self.status = "Failed"
            print("International Card Payment failed.")


card_txn = CardTransaction(
    txn_id="TXN1001",
    amount=5000,
    card_number=1234567812345678
)

card_txn.process()
card_txn.verify_card()



# ====================sample output===============
# Processing Transaction ID: TXN1001, Amount: 5000, Status: Pending
# Card verification successful.