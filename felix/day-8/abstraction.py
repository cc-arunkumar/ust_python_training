# importing abstract class 
from abc import ABC,abstractmethod

# Declaring abstract class
class Payment:
    # Creating abstract method
    @abstractmethod
    def pay_bill(self,amount):
        pass
    
# Implementations for abstract method in different class
class CareditCardPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using card payment")
    
class CashPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using cash")

class DigitalWalletPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using Digital Wallet")
    
class UpiPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using UPI")
    
# Creating objects for each derrived class
credit_card_payment = CareditCardPayment()
credit_card_payment.pay_bill(1000)

cash_payment = CashPayment()
cash_payment.pay_bill(2000)

digital_wallet_payment = DigitalWalletPayment()
digital_wallet_payment.pay_bill(3000)

upi_payment = UpiPayment()
upi_payment.pay_bill(4000)

# output

# Paying bill of amount 1000 using card payment
# Paying bill of amount 2000 using cash
# Paying bill of amount 3000 using Digital Wallet
# Paying bill of amount 4000 using UPI