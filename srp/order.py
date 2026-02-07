class Order:
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

class PriceCalculator:
    @staticmethod
    def calculate_total(order: Order) -> float:
        return order.quantity * order.price * 0.9

class PaymentProcessor:
    @staticmethod
    def process_payment(payment_details: str):
        print(f"Payment processed using: {payment_details}")

class NotificationSender:
    @staticmethod
    def send_confirmation_email(email: str):
        print(f"Confirmation email sent to: {email}")

if __name__ == "__main__":
    order = Order("Laptop", 2, 1000)
    total = PriceCalculator.calculate_total(order)
    print(f"Total: {total}")
    PaymentProcessor.process_payment("Credit Card")
    NotificationSender.send_confirmation_email("customer@example.com")
