# 🧩 Question:
# Create an abstract class `Payment` with an abstract method `pay_bill(amount)`.
# Implement four subclasses: `UpiPayment`, `CashPayment`, `WalletPayment`, and `CreditCardPayment`.
# Each subclass should override `pay_bill()` to print how the payment is made.
# Create objects of each subclass and call `pay_bill()` to demonstrate abstraction and polymorphism.

from abc import ABC, abstractmethod

# Abstract base class
class Payment(ABC):
    @abstractmethod
    def pay_bill(self, amount):
        pass  # Abstract method to be implemented by all subclasses

# Subclass for UPI payments
class UpiPayment(Payment):
    def pay_bill(self, amount):
        print(f"paying bill of amount {amount} using upi")

# Subclass for Cash payments
class CashPayment(Payment):
    def pay_bill(self, amount):
        print(f"paying bill of amount {amount} using cash")

# Subclass for Wallet payments
class WalletPayment(Payment):
    def pay_bill(self, amount):
        print(f"paying bill of amount {amount} using WalletPayment")

# Subclass for Credit Card payments
class CreditCardPayment(Payment):
    def pay_bill(self, amount):
        print(f"paying bill of amount {amount} using CreditCardPayment")

# Create object of CashPayment and call pay_bill
cashpayment = CashPayment()
cashpayment.pay_bill(2000)  
# Output: paying bill of amount 2000 using cash

# Create object of UpiPayment and call pay_bill
upipayment = UpiPayment()
upipayment.pay_bill(20000)  
# Output: paying bill of amount 20000 using upi

# Create object of WalletPayment and call pay_bill
walletpayment = WalletPayment()
walletpayment.pay_bill(100000)  
# Output: paying bill of amount 100000 using WalletPayment
# paying bill of amount 2000 using cash
# paying bill of amount 20000 using upi
# paying bill of amount 100000 using WalletPayment