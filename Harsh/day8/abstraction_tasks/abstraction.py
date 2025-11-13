from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay_bill(self, amount):
        pass
class CreditCardPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying {amount} using Credit Card.")
class CashPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying {amount} using Cash.")
class DigitalWalletPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying {amount} using Digital Wallet.")
class UPIPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying {amount} using UPI.")
    
    

ccp=CreditCardPayment()
ccp.pay_bill(1234)
cp=CashPayment()
cp.pay_bill(5678)
dwp=DigitalWalletPayment()
dwp.pay_bill(9012)
upi=UPIPayment()
upi.pay_bill(3456)



# Paying 1234 using Credit Card.
# Paying 5678 using Cash.
# Paying 9012 using Digital Wallet.
# Paying 3456 using UPI.l