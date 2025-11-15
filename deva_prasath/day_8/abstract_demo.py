# Import ABC and abstractmethod from abc module for creating abstract classes
from abc import ABC, abstractmethod

# Abstract class Payment, inheriting from ABC (Abstract Base Class)
class Payment(ABC):
    
    # Abstract method that must be implemented by all subclasses
    @abstractmethod
    def pay_bill(self, amount):
        pass  # This will be overridden in the subclasses

# Concrete class for Credit Card payment, inherits from Payment
class CreditCard(Payment):
    
    # Overriding the abstract method to implement the payment logic
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using Credit Card")
    
# Concrete class for Cash payment, inherits from Payment
class CashAmount(Payment):
    
    # Overriding the abstract method to implement the payment logic
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using Cash")

# Concrete class for Digital Wallet payment, inherits from Payment
class DigitalWalletPayment(Payment):
    
    # Overriding the abstract method to implement the payment logic
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using Digital Wallet")

# Concrete class for UPI payment, inherits from Payment
class UPIPayment(Payment):
    
    # Overriding the abstract method to implement the payment logic
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using UPI")

# Creating an instance of CreditCard and making payment
credit = CreditCard()
credit.pay_bill(1000)  # Paying bill of 1000 using Credit Card

# Creating an instance of CashAmount and making payment
cash = CashAmount()
cash.pay_bill(2000)  # Paying bill of 2000 using Cash

# Creating an instance of DigitalWalletPayment and making payment
digi = DigitalWalletPayment()
digi.pay_bill(3000)  # Paying bill of 3000 using Digital Wallet

# Creating an instance of UPIPayment and making payment
upi = UPIPayment()
upi.pay_bill(4000)  # Paying bill of 4000 using UPI
