# Demonstration of abstraction

from abc import ABC, abstractmethod
class Payment(ABC):
    def pay_bill(self,amount):
        pass
class Creditcard(Payment):
    def pay_bill(self,amount):
        print(f"paying bill of amount {amount} using credit card")
class UPI(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using UPI")
class Cash(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using cash ")
class PayPal(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount {amount} using cash")

credit_card_payment=Creditcard()
credit_card_payment.pay_bill(10000)
upi_payment=UPI()
upi_payment.pay_bill(1000000)
cash=Cash()
cash.pay_bill(130000)
pay_pal_payment=PayPal()
pay_pal_payment.pay_bill(2000)



# Output
# paying bill of amount 10000 using credit card
# Paying bill of amount 1000000 using UPI
# Paying bill of amount 130000 using cash 
# Paying bill of amount 2000 using cash