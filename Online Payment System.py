class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement this method")


class CreditCardPayment(Payment):
    def pay(self, amount):
        processing_fee = amount * 0.02   # 2% fee
        total = amount + processing_fee
        print("Processing Credit Card Payment...")
        print("Amount:", amount)
        print("Processing Fee (2%):", processing_fee)
        print("Total Deducted:", total)
        print("Payment Successful via Credit Card\n")


class UPIPayment(Payment):
    def pay(self, amount):
        print("Processing UPI Payment...")
        print("Amount:", amount)
        print("No processing fee for UPI.")
        print("Payment Successful via UPI\n")


class WalletPayment(Payment):
    def pay(self, amount):
        cashback = amount * 0.05  # 5% cashback
        print("Processing Wallet Payment...")
        print("Amount:", amount)
        print("Cashback Earned (5%):", cashback)
        print("Payment Successful via Wallet\n")


def process_payment(payment_method, amount):
    payment_method.pay(amount)


credit = CreditCardPayment()
upi = UPIPayment()
wallet = WalletPayment()

process_payment(credit, 1000)
process_payment(upi, 500)
process_payment(wallet, 800)
