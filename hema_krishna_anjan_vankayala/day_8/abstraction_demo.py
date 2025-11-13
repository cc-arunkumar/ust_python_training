from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass

class UPIPayment(Payment):
    def pay_bill(self, amount):
        print("UPI Payment of",amount,"Received!")

class CashPayemnt(Payment):
    def pay_bill(self, amount):
        print("Cash Payment of",amount,"Received!")
        
class CreditCardPayment(Payment):
    def pay_bill(self, amount):
        print("Credit Card Payment of",amount,"Received!")
        
#payment = Payment()  #throws an Error since we cant instantiate an abstract class 

credit_card = CreditCardPayment()
credit_card.pay_bill(1000)

#Sample Output
# Credit Card Payment of 1000 Received!