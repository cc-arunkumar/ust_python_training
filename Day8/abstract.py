#Abstract class
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay_bill(self):
        pass

class CreditCard(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount: {amount} using \"Creditcard\"")
class CashPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using cashpayment")
class DigitalWalletPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using cashpayment")
class UpiPayemnt(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using Upipayment")

credit_card_payment = CreditCard()
credit_card_payment.pay_bill(1234)

#sample output:
# Paying bill of amount: 1234 using "Creditcard"
        