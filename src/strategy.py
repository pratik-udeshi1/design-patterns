from abc import ABC, abstractmethod


# Strategy 1: PaymentMethod
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# Concrete Strategy 1: Credit Card Payment
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ₹{amount}")


# Concrete Strategy 2: PayPal Payment
class UPIPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ₹{amount}")


# Concrete Strategy 3: Cryptocurrency Payment
class CashPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing cash payment of ₹{amount}")


# Context: PaymentProcessor
class PaymentProcessor:

    def __init__(self):
        self.payment_method = None

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def make_payment(self, amount):
        self.payment_method.process_payment(amount)


# Example usage
credit_card = CreditCardPayment()
upi = UPIPayment()
cash = CashPayment()

payment_processor = PaymentProcessor()
payment_processor.set_payment_method(upi)
payment_processor.make_payment(50)
# Outputs: Processing UPI payment of ₹50

payment_processor.set_payment_method(cash)
payment_processor.make_payment(200)
# Outputs: Processing cash payment of ₹200


payment_processor.set_payment_method(credit_card)
payment_processor.make_payment(500)
# Outputs: Processing credit card payment of ₹500
