#Implementing abstraction method


# Importing ABC module to create abstract base classes
from abc import ABC,abstractmethod

# Defining an abstract base class 'Payment'
class Payment:
    # Abstract method that must be implemented by subclasses
    @abstractmethod
    def pay_bill(self,amount):
        pass

# Subclass implementing payment via credit card
class CreditCardPayment(Payment):
    def pay_bill(self,amount):
        print(f"paying bill of amount {amount} using credit card.\n")

# Subclass implementing payment via cash
class CashPayment(Payment):
    def pay_bill(self,amount):
        print(f"paying bill of amount {amount} using cash.\n")

# Subclass implementing payment via netbanking     
class Netbanking(Payment):
    def pay_bill(self,amount):
        print(f"paying bill of amount {amount} using netbanking.")

# Creating an object of CreditCardPayment and calling pay_bill
credit_card_payment=CreditCardPayment()
credit_card_payment.pay_bill(1000)

# Creating an object of CashPayment and calling pay_bill
cash_payment=CashPayment()
cash_payment.pay_bill(450)

# Creating an object of Netbanking and calling pay_bill
net_banking=Netbanking()
net_banking.pay_bill(3000)

#o/p:
# paying bill of amount 1000 using credit card.

# paying bill of amount 450 using cash.

# paying bill of amount 3000 using netbanking.