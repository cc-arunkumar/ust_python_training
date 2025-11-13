# abstraction
from abc import ABC, abstractmethod
# abstract method
class Payment(ABC):
    def pay_bill(self,amount):
        pass 
# child class
class CreditCardPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount{amount} using credit card.")
class CashPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount{amount} using cash.")
class DigitalWalletPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount{amount} using digital Wallet")
class UPIPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount{amount} using UPI.")
credit_card_payment=CreditCardPayment()
credit_card_payment.pay_bill(1000)
cp=CashPayment()
cp.pay_bill(2000)
dwp=DigitalWalletPayment()
dwp.pay_bill(3000)
upi=UPIPayment()
upi.pay_bill(4000)

# sample output
# Paying bill of amount1000 using credit card.
# Paying bill of amount2000 using cash.
# Paying bill of amount3000 using digital Wallet
# Paying bill of amount4000 using UPI.
