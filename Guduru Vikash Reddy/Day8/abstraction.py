# Step 1: Define an abstract base class Payment with an abstract method pay_bill
from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass

# Step 2: Implement the pay_bill method in CreditCard subclass
class CreditCard(Payment):
    def pay_bill(self, amount):
        print("The amount is paid by credit card:",amount)

# Step 3: Implement the pay_bill method in CashPayment subclass
class CashPayment(Payment):
    def pay_bill(self, amount):
        print("The amount is paid by cash payment:",amount)

# Step 4: Implement the pay_bill method in DigitalWalletPayment subclass
class DigitalWalletPayment(Payment):
    def pay_bill(self, amount):
        print("The amount is paid by Digital wallwt payment:",amount)

# Step 5: Implement the pay_bill method in UpiPayment subclass and demonstrate usage
class UpiPayment(Payment):
    def pay_bill(self, amount):
        print("The amount is paid by upi payment:",amount)

creditcard=CreditCard()
creditcard.pay_bill(400)

upipayment=UpiPayment()
upipayment.pay_bill(700)      

# sample output
# The amount is paid by credit card: 400
# The amount is paid by upi payment: 700  