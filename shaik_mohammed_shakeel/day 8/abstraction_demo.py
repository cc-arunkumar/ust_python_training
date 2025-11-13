#Abstraction

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass

class CreditCard(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount: {amount} using credit card")
class CashPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount: {amount} using Cash Payment")
class DigitalWalletPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount: {amount} using Digital Wallet Payment")
class UPIPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount: {amount} using UPI Payment")

# payment=Payment() #This will raise error coz we cannot instatiate abstract class
credit_payment=CreditCard()
credit_payment.pay_bill(1000)

upi_payment=UPIPayment()
upi_payment.pay_bill(2000)

cash_payment=CashPayment()
cash_payment.pay_bill(5000)

dwp=DigitalWalletPayment()
dwp.pay_bill(500)