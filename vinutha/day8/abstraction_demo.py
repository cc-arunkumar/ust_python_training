# abstraction
from abc import ABC, abstractmethod   # Import ABC (Abstract Base Class) and abstractmethod

# Abstract base class
class Payment(ABC):
    # Abstract method (must be implemented by child classes)
    @abstractmethod
    def pay_bill(self, amount):
        pass   # Placeholder, no implementation here


# Child class: CreditCardPayment
class CreditCardPayment(Payment):
    # Implement abstract method
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using credit card.")


# Child class: CashPayment
class CashPayment(Payment):
    # Implement abstract method
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using cash.")


# Child class: DigitalWalletPayment
class DigitalWalletPayment(Payment):
    # Implement abstract method
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using digital wallet.")


# Child class: UPIPayment
class UPIPayment(Payment):
    # Implement abstract method
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using UPI.")


# Create objects of different payment types and call their methods
credit_card_payment = CreditCardPayment()
credit_card_payment.pay_bill(1000)   # Credit card payment

cp = CashPayment()
cp.pay_bill(2000)                    # Cash payment

dwp = DigitalWalletPayment()
dwp.pay_bill(3000)                   # Digital wallet payment

upi = UPIPayment()
upi.pay_bill(4000)                   # UPI payment


# sample output
# Paying bill of amount1000 using credit card.
# Paying bill of amount2000 using cash.
# Paying bill of amount3000 using digital Wallet
# Paying bill of amount4000 using UPI.
