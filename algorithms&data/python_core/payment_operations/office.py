
from payment_process import CreditCardPayment, CryptoPayment


order_1 = CreditCardPayment(amount=23.23,
                           currency="USD",
                           name="Jane",
                           card_number="2223 2323 2323 2323",
                           cvv=499,
                           expiry="08/28")

order_2 = CryptoPayment(amount=2,
                        currency="ETH",
                        wallet_adress="0x_vu98ryewrhgv84rbv384",
                        name="James")


order_1.process()
order_2.process()


if __name__ == "__main__":
    print(order_1)
    print(order_2)