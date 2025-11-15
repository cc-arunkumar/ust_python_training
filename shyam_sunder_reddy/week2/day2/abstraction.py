from abc import ABC,abstractmethod

#Abstract class
class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass
class CardPayment(Payment):
    def pay_bill(self, amount):
        print("payed bill using card",amount)
class OnlinePayment(Payment):
    def pay_bill(self, amount):
        print("payed bill using Online",amount)
class UpiPayment(Payment):
    def pay_bill(self, amount):
        print("payed bill using Upi",amount)
class CashPayment(Payment):
    def pay_bill(self, amount):
        print("payed bill using Cash",amount)
        

cc=CardPayment()
cc.pay_bill(3000)

oc=OnlinePayment()
oc.pay_bill(5000)

upi=UpiPayment()
upi.pay_bill(8000)

cash=CashPayment()
cash.pay_bill(90)

#Sample output
# payed bill using card 3000
# payed bill using Online 5000
# payed bill using Upi 8000   
# payed bill using Cash 90    
