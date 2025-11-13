from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass
    
class CreditCardPayment(Payment):
    def pay_bill(self, amount):
        print(f"Payment bill of {amount} using Credit Card")

class CashPayment(Payment):
    def pay_bill(self, amount):
        print(f"Payment bill of {amount} using Cash")


class DigitalWalletPayment(Payment):
    def pay_bill(self, amount):
        print(f"Payment bill of {amount} using Digital Wallet")
        

class UPIPayment(Payment):
    def pay_bill(self, amount):
        print(f"Payment bill of {amount} using UPI")
        
credit = CreditCardPayment()
credit.pay_bill(1000)

cash = CashPayment()
cash.pay_bill(1000)

digital = DigitalWalletPayment()
digital.pay_bill(1000)

upi = UPIPayment()
upi.pay_bill(1000)

# Output
# Payment bill of 1000 using Credit Card
# Payment bill of 1000 using Cash
# Payment bill of 1000 using Digital Wallet
# Payment bill of 1000 using UPI