#A simple task on Execution of Abstraction

from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod             #abstractmethod
    def pay_bill(Self,amount):
        pass 
    
class CreditCardPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using Credit card")
        
class CashPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using Cash")

class DigitalWalletPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using Digital Wallet")

class UPIPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using UPI")
    
# payment=Payment() raises an error

#calling abstract class
credit_card_payment=CreditCardPayment()
credit_card_payment.pay_bill(1000)

