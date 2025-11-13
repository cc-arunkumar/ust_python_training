from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass 

class CreditCardPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount{amount} using credit card")
class CashPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount{amount} using cash")
class DigitalwalletPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount{amount} using digit wallet")
class UPIPayment(Payment):
    def pay_bill(self,amount):
        print(f"Paying bill of amount{amount} using upi")
    


credit_card_payment=CreditCardPayment()
credit_card_payment.pay_bill(30000)
cash_payment=CashPayment()
cash_payment.pay_bill(90000)
digital_card=DigitalwalletPayment()
digital_card.pay_bill(10000)
upi_payment=UPIPayment()
upi_payment.pay_bill(50000)




# sample execution 
# Paying bill of amount30000 using credit card
# Paying bill of amount90000 using cash
# Paying bill of amount10000 using digit wallet
# Paying bill of amount50000 using upi


