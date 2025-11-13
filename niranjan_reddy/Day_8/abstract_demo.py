# Abstraction 

from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass

class CreaditCardPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using Credit Card")

class CashPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using Cash")

class UPIPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using UPI")

class DigitalWalletPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using Digital Wallet")

# payment=Payment()         #This will raise an error since we cannot instantiate an abstract class


upi_payment=UPIPayment()

upi_payment.pay_bill(1200)

cash_payment=CashPayment()

cash_payment.pay_bill(500)

# Sample output

# Paying bill of amount 1200 using UPI
# Paying bill of amount 500 using Cash