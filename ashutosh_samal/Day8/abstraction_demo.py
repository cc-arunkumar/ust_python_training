from abc import ABC, abstractmethod
#abstract class creation
class Payment(ABC):
    @abstractmethod
    def pay_bill(self,amount):
        pass

#class credit card inherited from payment
class CreditCardPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of {amount} using Credit Card.")

#class cash payment inherited from payment
class CashPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of {amount} using Cash.")

#class digital payment inherited from payment        
class DigitalWalletPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of {amount} using Digital Wallet.")

#class upi payment inherited from payment
class UPIPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying bill of {amount} using UPI.")

#object creation and Calling the functions  
ccp1 = CreditCardPayment()
ccp1.pay_bill(5000)

cp1 = CashPayment()
cp1.pay_bill(1500)

wp1 = CashPayment()
wp1.pay_bill(500)

upi1 = UPIPayment()
upi1.pay_bill(25000)


#Sample Execution
# Paying bill of 5000 using Credit Card.
# Paying bill of 1500 using Cash.
# Paying bill of 500 using Cash. 
# Paying bill of 25000 using UPI.