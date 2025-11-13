# abstractration example
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def Pay_bill(self,amount):
        pass
class OnlinePayment(Payment):
    def Pay_bill(self, amount):
        print(f"the bill {amount} is paid using the online payment")
class UPIPayment(Payment):
    def Pay_bill(self, amount):
        print(f"the bill {amount} is paid using the upi payment")
class CashPayment(Payment):
    def Pay_bill(self, amount):
        print(f"the bill {amount} is paid using the cash")

pay=CashPayment()
pay.Pay_bill(1000)

pay1=OnlinePayment()
pay1.Pay_bill(120000)

# output
# the bill 1000 is paid using the cash
# the bill 120000 is paid using the online payment