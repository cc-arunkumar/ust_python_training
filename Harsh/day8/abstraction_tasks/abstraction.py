from abc import ABC, abstractmethod

# Abstract base class for Payment
class Payment(ABC):
    # Abstract method that must be implemented by all subclasses
    @abstractmethod
    def pay_bill(self, amount):
        pass


# Subclass for Credit Card Payment
class CreditCardPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying {amount} using Credit Card.")


# Subclass for Cash Payment
class CashPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying {amount} using Cash.")


# Subclass for Digital Wallet Payment
class DigitalWalletPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying {amount} using Digital Wallet.")


# Subclass for UPI Payment
class UPIPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying {amount} using UPI.")


# ------------------- Testing -------------------
ccp = CreditCardPayment()
ccp.pay_bill(1234)

cp = CashPayment()
cp.pay_bill(5678)

dwp = DigitalWalletPayment()
dwp.pay_bill(9012)

upi = UPIPayment()
upi.pay_bill(3456)




# Paying 1234 using Credit Card.
# Paying 5678 using Cash.
# Paying 9012 using Digital Wallet.
# Paying 3456 using UPI.l