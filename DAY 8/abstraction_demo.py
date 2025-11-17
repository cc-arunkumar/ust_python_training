from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass

class CreditCardPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of {amount} by using Credit Card")

class CashPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of {amount} by using Cash Mode")

class UPIPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of {amount} by using UPI Payment")

class DigitalWalletPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of {amount} by using Digital Wallet")

# Created an object for UPI payment
upi_payment=UPIPayment()
upi_payment.pay_bill(1000)


"""
SAMPLE OUTPUT

Paying bill of 1000 by using UPI Payment
"""