from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass
class Upi_payment(Payment):
    def pay_bill(self, amount):
        print("Upi _payment:",self.amount)

class Cash_payment(Payment):
    def pay_bill(self, amount):
        print("Cash_payment",amount)
class Credit_payment(Payment):
    def pay_bill(self,amount):
        print("Credit_payment:",amount)


c1=Credit_payment()
c1.pay_bill(3000)
c2=Upi_payment()
c2=Credit_payment()