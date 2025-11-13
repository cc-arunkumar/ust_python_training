from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass 
class CredictCardPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using credit Card")
class CashPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using Cash ")
class DigitalPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using Digital Payment")
class Upipayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using upi Payment")

cash_payment = CashPayment()
print(cash_payment.pay_bill(5000))