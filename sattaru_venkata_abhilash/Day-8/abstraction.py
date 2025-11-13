from abc import ABC, abstractmethod

# ---------------------------------------
# Abstract Base Class
# ---------------------------------------
class Payments(ABC):

    @abstractmethod
    def pay_bill(self, amount):
        pass


# ---------------------------------------
# Child Classes Implementing Abstract Method
# ---------------------------------------
class CreditCardPayment(Payments):
    def pay_bill(self, amount):
        print(f"Paying bill of amount ₹{amount} using Credit Card.")


class CashPayment(Payments):
    def pay_bill(self, amount):
        print(f"Paying bill of amount ₹{amount} using Cash.")


class DigitalWalletPayment(Payments):
    def pay_bill(self, amount):
        print(f"Paying bill of amount ₹{amount} using Digital Wallet.")


class UPIPayment(Payments):
    def pay_bill(self, amount):
        print(f"Paying bill of amount ₹{amount} using UPI.")


# ---------------------------------------
# Object Creation + Method Calls
# ---------------------------------------
credit = CreditCardPayment()
credit.pay_bill(1000)

cash = CashPayment()
cash.pay_bill(500)

wallet = DigitalWalletPayment()
wallet.pay_bill(1500)

upi = UPIPayment()
upi.pay_bill(250)


# Sample Output:
# Paying bill of amount ₹1000 using Credit Card.
# Paying bill of amount ₹500 using Cash.
# Paying bill of amount ₹1500 using Digital Wallet.
# Paying bill of amount ₹250 using UPI.
