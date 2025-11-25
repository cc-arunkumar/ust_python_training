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
        
class UPIpayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying {amount} using UPI.")
        
class WalletPayment(Payment):
    def pay_bill(self, amount):
        print(f"Paying {amount} using Wallet.")
        
# Example usage:
credit_card_payment = CreditCardPayment()
credit_card_payment.pay_bill(1000)
cash_payment = CashPayment()
cash_payment.pay_bill(500)  
upi_payment = UPIpayment()
upi_payment.pay_bill(750)
wallet_payment = WalletPayment()
wallet_payment.pay_bill(300)


#Sample Output:
# Paying 1000 using Credit Card.
# Paying 500 using Cash.
# Paying 750 using UPI.
# Paying 300 using Wallet.