from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass
class UpiPayment(Payment):
    def pay_bill(self,amount):
        print(f"paying bill of amount {amount} using upi")
class CashPayment(Payment):
    def pay_bill(self,amount):
        print(f"paying bill of amount {amount} using cash")
class WalletPayment(Payment):
    def pay_bill(self,amount):
        print(f"paying bill of amount {amount} using WalletPayment")
class CreditCardPayment(Payment):
    def pay_bill(self,amount):
        print(f"paying bill of amount {amount} using CreditCardPayment")
        
cashpayment=CashPayment()
cashpayment.pay_bill(2000)
upipayment=UpiPayment()
upipayment.pay_bill(20000)
walletpayment=WalletPayment()
walletpayment.pay_bill(100000)