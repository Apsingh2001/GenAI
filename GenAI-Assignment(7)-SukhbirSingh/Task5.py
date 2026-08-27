'''Abstraction (Using Abstract Base Class)
- Create an abstract class Payment with abstract method:
    process_payment(amount)
- Then create two subclasses:
    CreditCardPayment
    UPIPayment
- Both override process_payment() with simple print statements.
- Test all classes.'''

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount:.2f}")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ${amount:.2f}")


credit_card_payment = CreditCardPayment()
upi_payment = UPIPayment()

credit_card_payment.process_payment(100.00)
upi_payment.process_payment(250.50)