# Abstraction

from abc import ABC,abstractmethod

class Payment:
    @abstractmethod
    def pay_bill(self,amount):
        pass

class CreditCardPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using Credit Card")

class CashPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using Cash Payment")

class DigitWallePayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using Digit Wallet Payment")

class UPIPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of amount {amount} using UPI Payment")

# Payment = Payment() #This will raise an error since we cannot instantiate an abstract class

credit_card_payment = CreditCardPayment()
credit_card_payment.pay_bill(10000)

upi_payment = UPIPayment()
upi_payment.pay_bill(5000)

# ------------------------------------------------------------------------------------

# Sample Output

# Paying bill of amount 10000 using Credit Card
# Paying bill of amount 5000 using UPI Payment
