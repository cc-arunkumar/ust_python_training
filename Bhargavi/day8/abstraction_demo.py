#abstarction demo problem to show how the methods are work in the presences of abstract class

from abc import ABC , abstractmethod

#abstract class
class Payment(ABC):
    @abstractmethod
    def payment(self , amount):
        pass

#child class
class Debitcardpayment(Payment):
    def payment(self , amount):
        print(f"  The payment is done using debitcard of amonut {amount}.")

#childclass of payment
class UPIpayment(Payment):
    def payment(self , amount):
        print(f" The payment is done using UPI of amonut {amount}.")

#wallet class
class Wallet(Payment):
    def payment(self , amount):
        print(f" The payment is done using wallet of amonut {amount}.")

class Bheemapay(Payment):
    def payment(self , amount):
        print(f" The payment is done using Bheemapay of amonut {amount}.")

#creating objects and calling the methods
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
