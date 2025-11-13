from abc import ABC,abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass

class online_payment(Payment):
     def pay_bill(self,amount):
            print("Paid through online")

class cash_payment(Payment):
     def pay_bill(self,amount):
            print("Paid through Cash")


pay=online_payment()
pay.pay_bill(1000)
pay1=cash_payment()
pay1.pay_bill(2000)       