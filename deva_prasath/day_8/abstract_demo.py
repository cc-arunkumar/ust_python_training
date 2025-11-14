from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass

class CreditCard(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using Credit Card")
    
class CashAmount(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using Cash")

class DigitalWalletPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using Digital Wallet")

class UPIPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using UPI")


credit=CreditCard()
credit.pay_bill(1000)

cash=CashAmount()
cash.pay_bill(2000)

digi=DigitalWalletPayment()
digi.pay_bill(3000)

upi=UPIPayment()
upi.pay_bill(4000)