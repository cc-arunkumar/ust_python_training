#Task : Abstraction 

#Code
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass
class CreditCardPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using credit card")
class CashPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using Cash")
class DigitalWallet(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using digitalwallet")
class UPIPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill amount {amount} using UPI")

credit_card_payment =CreditCardPayment()
credit_card_payment.pay_bill(1000)
cash_payment=CashPayment()
cash_payment.pay_bill(233)
digital_wallet=DigitalWallet()
digital_wallet.pay_bill(34)
upi_payment = UPIPayment()
upi_payment.pay_bill(466)

#Output
# Paying bill of amount 1000 using credit card
# Paying bill of amount 233 using Cash        
# Paying bill of amount 34 using digitalwallet
# Paying bill amount 466 using UPI