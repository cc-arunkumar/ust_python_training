from abc import ABC, abstractmethod   # Import abstract base class utilities

# Abstract base class representing a generic Payment
class Payment(ABC):
    @abstractmethod
    def pay_bill(self, amount):
        # Abstract method that must be implemented by subclasses
        pass 

# Subclass for Credit Card payments
class CredictCardPayment(Payment):
    def pay_bill(self, amount):
        # Implementation of abstract method for credit card
        print(f"Paying bill of amount {amount} using credit Card")

# Subclass for Cash payments
class CashPayment(Payment):
    def pay_bill(self, amount):
        # Implementation of abstract method for cash
        print(f"Paying bill of amount {amount} using Cash ")

# Subclass for Digital Wallet payments
class DigitalPayment(Payment):
    def pay_bill(self, amount):
        # Implementation of abstract method for digital payment
        print(f"Paying bill of amount {amount} using Digital Payment")

# Subclass for UPI payments
class Upipayment(Payment):
    def pay_bill(self, amount):
        # Implementation of abstract method for UPI
        print(f"Paying bill of amount {amount} using upi Payment")


# Create an object of CashPayment
cash_payment = CashPayment()

# Call pay_bill method with amount = 5000
# Note: pay_bill prints the message but returns None, so print() around it will show "None"
print(cash_payment.pay_bill(5000))



# =======sample output=============
# Paying bill of amount 5000 using Cash 

