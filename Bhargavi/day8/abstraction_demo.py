# This program demonstrates abstraction using Python’s abc module, where the Payment class defines a common interface.
# Each subclass implements its own payment() method, showing different ways of processing payments.

from abc import ABC , abstractmethod

#abstract class
class Payment(ABC):
    @abstractmethod
    def payment(self , amount):
        pass

#child class for debitcard
class Debitcardpayment(Payment):
    def payment(self , amount):
        print(f"  The payment is done using debitcard of amonut {amount}.")
        
# Child class for UPI payment 
class UPIpayment(Payment):
    def payment(self , amount):
        print(f" The payment is done using UPI of amonut {amount}.")
      

# Child class for Wallet payment  
class Wallet(Payment):
    def payment(self , amount):
        print(f" The payment is done using wallet of amonut {amount}.")

# Child class for Bheemapay payment
class Bheemapay(Payment):
    def payment(self , amount):
        print(f" The payment is done using Bheemapay of amonut {amount}.")
        
# Create objects of different payment types and call their methods
pay2 = Debitcardpayment()
pay2.payment(10000)

pay3 = UPIpayment()
pay3.payment(60000)

pay4= Wallet()
pay4.payment(70000)

pay5 = Bheemapay()
pay5.payment(40000)

#  The payment is done using debitcard of amonut 10000.
#  The payment is done using UPI of amonut 60000.
#  The payment is done using wallet of amonut 70000.
#  The payment is done using Bheemapay of amonut 40000.