from abc import ABC,abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay_bill(self,amount):
        pass

class UpiPayment(Payment):

    def pay_bill(self,amount):
        print(f"Payment of Rs{amount} done through UPI")

class CashPayment(Payment):

    def pay_bill(self,amount):
        print(f"Payment of Rs{amount} done through Cash")

class NetBankingPayment(Payment):

    def pay_bill(self,amount):
        print(f"Payment of Rs{amount} done through Net Banking")

NetBankingPayment().pay_bill(1000)
CashPayment().pay_bill(1200)
UpiPayment().pay_bill(5000)

#Output
# Payment of Rs1000 done through Net Banking
# Payment of Rs1200 done through Cash
# Payment of Rs5000 done through UPI