#Task Data Abstraction
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass
class CreditCardPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using Credit card.")
class CashPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using Cash.")

class DigitalWalletPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using Digital Wallet.")
class UPIPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using UPI.")
credit_card_payment=CreditCardPayment()
credit_card_payment.pay_bill(1000)
cash_payment=CashPayment()
cash_payment.pay_bill(1000)
digital_wallet_payment=DigitalWalletPayment()
digital_wallet_payment.pay_bill(1000)
upi_payment=UPIPayment()
upi_payment.pay_bill(1000)
    
#Sample Execution
# Paying bill of amount 1000 using Credit card.
# Paying bill of amount 1000 using Cash.
# Paying bill of amount 1000 using Digital Wallet.
# Paying bill of amount 1000 using UPI.